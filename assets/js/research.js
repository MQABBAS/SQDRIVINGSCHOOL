/* SQ Driving Data Lab — interactive tools for the research pages */
(function () {
  "use strict";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var toMin = function (t) { var p = String(t).split(":"); return (+p[0]) * 60 + (+p[1]); };
  var pct = function (m) { return (m / 1440 * 100).toFixed(3) + "%"; };
  var hm = function (m) { return Math.floor(m / 60) + "h " + String(m % 60).padStart(2, "0") + "m"; };

  /* ---------- daylight & low-sun explorer ---------- */
  function sun(root) {
    var data; try { data = JSON.parse(root.getAttribute("data-months")); } catch (e) { return; }
    var chips = $(".rx-chips", root), out = {};
    ["sunrise", "sunset", "dusk", "daylight", "glare", "verdict"].forEach(function (k) { out[k] = $(".js-" + k, root); });
    var bar = $(".rx-day", root);
    var seg = function (cls) { var d = document.createElement("div"); d.className = "rx-day__seg " + cls; bar.appendChild(d); return d; };
    var twAm = seg("rx-day__tw"), day = seg("rx-day__sun"), twPm = seg("rx-day__tw rx-day__tw--pm"), gAm = seg("rx-day__glare"), gPm = seg("rx-day__glare");
    var test = document.createElement("div"); test.className = "rx-day__test"; test.title = "Typical driving test hours (about 08:00–16:00)"; bar.appendChild(test);
    var names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    data.forEach(function (m, i) { var b = document.createElement("button"); b.type = "button"; b.textContent = names[i]; b.setAttribute("aria-pressed", "false"); b.addEventListener("click", function () { show(i); }); chips.appendChild(b); });
    function place(el, a, b) { el.style.left = pct(a); el.style.width = pct(Math.max(0, b - a)); }
    function show(i) {
      var m = data[i];
      $$("button", chips).forEach(function (b, k) { b.classList.toggle("is-on", k === i); b.setAttribute("aria-pressed", String(k === i)); });
      var dawn = toMin(m.dawn), rise = toMin(m.sunrise), set = toMin(m.sunset), dusk = toMin(m.dusk);
      place(twAm, dawn, rise); place(day, rise, set); place(twPm, set, dusk);
      var g = function (s) { if (!s) return [0, 0]; var p = s.split("–"); return [toMin(p[0]), toMin(p[1])]; };
      var a = g(m.glare_am), p = g(m.glare_pm); place(gAm, a[0], a[1]); place(gPm, p[0], p[1]);
      place(test, 8 * 60, 16 * 60);
      out.sunrise.textContent = m.sunrise; out.sunset.textContent = m.sunset; out.dusk.textContent = m.dusk; out.daylight.textContent = hm(m.daylight_min);
      out.glare.textContent = (m.glare_am_min + m.glare_pm_min) ? Math.round((m.glare_am_min + m.glare_pm_min)) + " min" : "None";
      out.verdict.innerHTML = m.verdict;
    }
    var now = new Date().getMonth(); show(now);
  }

  /* ---------- pass-odds calculator ---------- */
  function odds(root) {
    var range = $("input[type=range]", root), lbl = $(".js-rate", root), fee = +root.getAttribute("data-fee") || 62;
    var bars = $$(".rx-odds div", root), exp = $(".js-exp", root), w2 = $(".js-w2", root), w3 = $(".js-w3", root), cost = $(".js-cost", root);
    function upd() {
      var p = +range.value / 100;
      lbl.textContent = (+range.value).toFixed(1) + "%";
      bars.forEach(function (d, k) { var v = 1 - Math.pow(1 - p, k + 1); $("i", d).style.height = (v * 100).toFixed(1) + "%"; $("b", d).textContent = Math.round(v * 100) + "%"; });
      exp.textContent = (1 / p).toFixed(2); w2.textContent = Math.round((1 - Math.pow(1 - p, 2)) * 100) + "%"; w3.textContent = Math.round((1 - Math.pow(1 - p, 3)) * 100) + "%";
      cost.textContent = "£" + Math.round(fee / p);
      $$(".rx-chips button", root).forEach(function (b) { b.classList.toggle("is-on", Math.abs(+b.getAttribute("data-rate") - +range.value) < .05); });
    }
    range.addEventListener("input", upd);
    $$(".rx-chips button", root).forEach(function (b) { b.addEventListener("click", function () { range.value = b.getAttribute("data-rate"); upd(); }); });
    upd();
  }

  /* ---------- instructor earnings calculator ---------- */
  function earn(root) {
    var f = function (n) { return Math.max(0, +($("[name=" + n + "]", root).value) || 0); };
    var gbp = function (n) { return (n < 0 ? "−£" : "£") + Math.abs(Math.round(n)).toLocaleString("en-GB"); };
    function upd() {
      var rate = f("rate"), hrs = f("hours"), wks = f("weeks"), car = f("car"), fuel = f("fuel"), fee = f("fee");
      var gross = rate * hrs * wks, costs = (car + fee) * 52 + fuel * hrs * wks, net = gross - costs;
      $(".js-gross", root).textContent = gbp(gross); $(".js-costs", root).textContent = gbp(costs); $(".js-net", root).textContent = gbp(net);
      $(".js-hourly", root).textContent = hrs && wks ? gbp(net / (hrs * wks)) + "/hr" : "—";
    }
    $$("input", root).forEach(function (i) { i.addEventListener("input", upd); });
    upd();
  }

  /* ---------- copy a citation ---------- */
  function cite(root) {
    var b = $("button", root), c = $("code", root); if (!b || !c) return;
    b.addEventListener("click", function () {
      var t = c.textContent;
      (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { b.textContent = "Copied ✓"; setTimeout(function () { b.textContent = "Copy citation"; }, 2000); }, function () { window.prompt("Copy this citation:", t); });
    });
  }

  function init() {
    $$("[data-rx=sun]").forEach(sun); $$("[data-rx=odds]").forEach(odds); $$("[data-rx=earn]").forEach(earn); $$("[data-rx=cite]").forEach(cite);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
