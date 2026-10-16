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


  /* ---------- stopping distance calculator (Highway Code model) ---------- */
  function stopping(root) {
    var sp = $("[name=speed]", root), rt = $("[name=react]", root), conds = $$("[data-cond]", root), cond = 1;
    function upd() {
      var mph = +sp.value, r = +rt.value, ms = mph * 0.44704;
      var think = ms * r, brake = 0.0153 * mph * mph * cond, total = think + brake, cars = total / 4;
      $(".js-mph", root).textContent = mph + " mph"; $(".js-rt", root).textContent = r.toFixed(2) + " s";
      $(".js-think", root).textContent = think.toFixed(0) + " m"; $(".js-brake", root).textContent = brake.toFixed(0) + " m";
      $(".js-total", root).textContent = total.toFixed(0) + " m"; $(".js-cars", root).textContent = cars.toFixed(1);
      var max = 0.44704 * 70 * 1.5 + 0.0153 * 4900 * 10, scale = Math.min(1, total / 150);
      $(".rx-stop__think", root).style.width = (think / Math.max(total, 1) * scale * 100) + "%";
      $(".rx-stop__brake", root).style.width = (brake / Math.max(total, 1) * scale * 100) + "%";
      $(".rx-stop__over", root).style.display = total > 150 ? "" : "none";
      var cars_el = $(".rx-stop__cars", root); cars_el.innerHTML = "";
      for (var i = 0; i < Math.min(40, Math.round(cars)); i++) { var c = document.createElement("i"); c.style.animationDelay = (i * 0.03) + "s"; cars_el.appendChild(c); }
      $$(".rx-hc tr", root).forEach(function (tr) { tr.classList.toggle("is-on", +tr.getAttribute("data-mph") === mph && cond === 1 && Math.abs(r - 0.67) < .01); });
    }
    conds.forEach(function (b) { b.addEventListener("click", function () { cond = +b.getAttribute("data-cond"); conds.forEach(function (x) { x.classList.toggle("is-on", x === b); }); upd(); }); });
    [sp, rt].forEach(function (i) { i.addEventListener("input", upd); });
    upd();
  }

  /* ---------- sun position in the browser (NOAA algorithm, Manchester) ---------- */
  var LAT = 53.4808, LON = -2.2426;
  function ukOffset(d) {
    var y = d.getUTCFullYear();
    function lastSun(m) { var x = new Date(Date.UTC(y, m + 1, 0, 1)); x.setUTCDate(x.getUTCDate() - x.getUTCDay()); return x; }
    return (d >= lastSun(2) && d < lastSun(9)) ? 1 : 0;
  }
  function sunElev(utcMs) {
    var jd = utcMs / 86400000 + 2440587.5, T = (jd - 2451545) / 36525, rad = Math.PI / 180;
    var L0 = (280.46646 + T * (36000.76983 + T * 0.0003032)) % 360, M = 357.52911 + T * (35999.05029 - 0.0001537 * T), e = 0.016708634 - T * (0.000042037 + 0.0000001267 * T);
    var C = Math.sin(M * rad) * (1.914602 - T * (0.004817 + 0.000014 * T)) + Math.sin(2 * M * rad) * (0.019993 - 0.000101 * T) + Math.sin(3 * M * rad) * 0.000289;
    var om = 125.04 - 1934.136 * T, lam = L0 + C - 0.00569 - 0.00478 * Math.sin(om * rad);
    var eps = 23 + (26 + (21.448 - T * (46.815 + T * (0.00059 - T * 0.001813))) / 60) / 60 + 0.00256 * Math.cos(om * rad);
    var dec = Math.asin(Math.sin(eps * rad) * Math.sin(lam * rad)), y = Math.pow(Math.tan(eps * rad / 2), 2);
    var eq = 4 / rad * (y * Math.sin(2 * L0 * rad) - 2 * e * Math.sin(M * rad) + 4 * e * y * Math.sin(M * rad) * Math.cos(2 * L0 * rad) - 0.5 * y * y * Math.sin(4 * L0 * rad) - 1.25 * e * e * Math.sin(2 * M * rad));
    var d = new Date(utcMs), mins = d.getUTCHours() * 60 + d.getUTCMinutes(), tst = ((mins + eq + 4 * LON) % 1440 + 1440) % 1440, ha = tst / 4 - 180;
    var cz = Math.sin(LAT * rad) * Math.sin(dec) + Math.cos(LAT * rad) * Math.cos(dec) * Math.cos(ha * rad);
    var el = 90 - Math.acos(Math.max(-1, Math.min(1, cz))) / rad;
    if (el > -0.575) { var te = Math.tan(el * rad); el += (el > 5 ? 58.1 / te - 0.07 / Math.pow(te, 3) + 0.000086 / Math.pow(te, 5) : 1735 + el * (-518.2 + el * (103.4 + el * (-12.79 + el * 0.711)))) / 3600; }
    var az = (Math.atan2(Math.sin(ha * rad), Math.cos(ha * rad) * Math.sin(LAT * rad) - Math.tan(dec) * Math.cos(LAT * rad)) / rad + 180) % 360;
    return [el, az];
  }
  function dayInfo(y, mo, da) {
    var probe = new Date(Date.UTC(y, mo, da, 12)), off = ukOffset(probe), base = Date.UTC(y, mo, da) - off * 3600000, el = [];
    for (var m = 0; m < 1440; m++) el.push(sunElev(base + m * 60000)[0]);
    var first = function (f) { for (var m = 0; m < 1440; m++) if (f(el[m])) return m; return -1; };
    var last = function (f) { for (var m = 1439; m >= 0; m--) if (f(el[m])) return m; return -1; };
    return { off: off, base: base, el: el, rise: first(function (e) { return e > -0.833; }), set: last(function (e) { return e > -0.833; }) + 1, dawn: first(function (e) { return e > -6; }), dusk: last(function (e) { return e > -6; }) + 1 };
  }
  var fmt = function (m) { return String(Math.floor(m / 60)).padStart(2, "0") + ":" + String(m % 60).padStart(2, "0"); };

  /* ---------- driving test day planner ---------- */
  function testday(root) {
    var dIn = $("[name=tdate]", root), tIn = $("[name=ttime]", root), out = $(".js-plan", root);
    var today = new Date(); if (!dIn.value) { var t = new Date(today.getTime() + 35 * 864e5); dIn.value = t.toISOString().slice(0, 10); }
    function upd() {
      if (!dIn.value || !tIn.value) return;
      var p = dIn.value.split("-").map(Number), tp = tIn.value.split(":").map(Number), tmin = tp[0] * 60 + tp[1];
      var info = dayInfo(p[0], p[1] - 1, p[2]), endMin = tmin + 40;
      var sAt = sunElev(info.base + tmin * 60000), sEnd = sunElev(info.base + Math.min(1439, endMin) * 60000);
      var light = function (e) { return e > 15 ? "Full daylight" : e > 0.5 ? "Low sun — glare possible" : e > -6 ? "Twilight — lights on" : "Dark"; };
      var dir = function (a) { return ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"][Math.round(a / 45) % 8]; };
      var dow = new Date(Date.UTC(p[0], p[1] - 1, p[2])).getUTCDay(), weekend = dow === 0 || dow === 6;
      var rush = !weekend && ((tmin >= 7 * 60 + 30 && tmin <= 9 * 60 + 15) || (tmin >= 15 * 60 && tmin <= 18 * 60 + 30));
      var schoolRun = !weekend && ((tmin >= 8 * 60 && tmin <= 9 * 60) || (tmin >= 14 * 60 + 45 && tmin <= 15 * 60 + 45));
      var warm = Math.max(0, tmin - 70), arrive = Math.max(0, tmin - 10), wake = Math.max(0, warm - 75);
      var notes = [];
      if (sAt[0] > 0.5 && sAt[0] <= 15) notes.push("☀️ The sun will be low in the <b>" + dir(sAt[1]) + "</b> (" + sAt[0].toFixed(0) + "° up) — keep sunglasses in the car and use the visor when you head that way.");
      if (sAt[0] <= 0.5 || sEnd[0] <= 0.5) notes.push("🌙 Part of your test is in twilight or darkness — make sure you've had at least one lesson in the dark and know how to use dipped headlights.");
      if (rush) notes.push("🚗 Rush-hour slot — expect queues, busy junctions and buses. Practise in the same hours the week before.");
      if (schoolRun) notes.push("🎒 School-run time — watch for children near schools and parked cars on residential roads.");
      if (weekend) notes.push("🗓️ Weekend test — lighter traffic but the DVSA charges £75 for evening, weekend and bank holiday tests.");
      var m1 = new Date(Date.UTC(p[0], p[1] - 1, p[2])), chg = [2, 9].map(function (mm) { var x = new Date(Date.UTC(p[0], mm + 1, 0)); x.setUTCDate(x.getUTCDate() - x.getUTCDay()); return x; });
      chg.forEach(function (c, i) { var diff = (m1 - c) / 864e5; if (diff >= 0 && diff < 14) notes.push(i ? "🕐 The clocks went back " + diff + " day(s) before your test — evenings are suddenly darker." : "🕐 The clocks went forward " + diff + " day(s) before your test — mornings are darker for a while."); });
      if (!notes.length) notes.push("✅ Good light and normal traffic — no special conditions to prepare for.");
      out.innerHTML = '<div class="rx-out"><div><b>' + fmt(info.rise) + '</b><span>Sunrise</span></div><div><b>' + fmt(info.set) + '</b><span>Sunset</span></div><div class="rx-big"><b>' + light(sAt[0]) + '</b><span>Light at the start of your test</span></div><div><b>' + light(sEnd[0]) + '</b><span>Light at the end (~40 min)</span></div></div>' +
        '<ol class="rx-steps mt-2"><li data-n="1"><h4>' + fmt(wake) + ' — wake up &amp; eat</h4><p>Give yourself time. Check your provisional licence is in your bag.</p></li><li data-n="2"><h4>' + fmt(warm) + ' — warm-up lesson</h4><p>Most SQ learners have a 1-hour lesson right before the test, ending at the test centre.</p></li><li data-n="3"><h4>' + fmt(arrive) + ' — arrive at the centre</h4><p>Arrive about 10 minutes early. Use the toilet, switch your phone off.</p></li><li data-n="4"><h4>' + fmt(tmin) + ' — your test begins</h4><p>Eyesight check, "show me, tell me" questions, about 40 minutes of driving including 20 minutes of independent driving.</p></li><li data-n="5"><h4>' + fmt(Math.min(1439, endMin)) + ' — result &amp; debrief</h4><p>You get your result straight away. Pass? Your instructor drives you home with the good news.</p></li></ol>' +
        '<div class="callout">' + notes.join("<br>") + "</div>";
    }
    [dIn, tIn].forEach(function (i) { i.addEventListener("input", upd); i.addEventListener("change", upd); });
    upd();
  }

  /* ---------- learning-to-drive timeline planner ---------- */
  function timeline(root) {
    var f = function (n) { return +$("[name=" + n + "]", root).value || 0; };
    function upd() {
      var need = Math.max(0, f("need") - f("done")), per = Math.max(0.5, f("perweek")), wait = f("wait");
      var weeks = Math.ceil(need / per), now = new Date(), ready = new Date(now.getTime() + weeks * 7 * 864e5);
      var bookBy = new Date(ready.getTime() - wait * 7 * 864e5), bookNow = bookBy <= now;
      var d = function (x) { return x.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" }); };
      $(".js-hrs", root).textContent = need + " hrs"; $(".js-weeks", root).textContent = weeks + " weeks";
      $(".js-ready", root).textContent = d(ready); $(".js-bookby", root).textContent = bookNow ? "Now" : d(bookBy);
      $(".js-cost", root).textContent = "£" + (need * 35).toLocaleString("en-GB");
      $(".js-tip", root).innerHTML = bookNow ? "📅 <b>Book your test now.</b> With a " + wait + "-week wait, the earliest date you can get is already close to when you'll be ready." : "📅 You should book your practical test around <b>" + d(bookBy) + "</b> so the date lands when you're ready. Pass your theory test first — it's needed before you can book.";
      var fill = $(".rx-tl__fill", root); fill.style.width = Math.min(100, (f("done") / Math.max(1, f("need"))) * 100) + "%";
    }
    $$("input", root).forEach(function (i) { i.addEventListener("input", upd); });
    upd();
  }

  /* ---------- hazard perception scoring window demo ---------- */
  function hazard(root) {
    var bar = $(".rx-hp__bar", root), btn = $(".js-hpgo", root), click = $(".js-hpclick", root), res = $(".js-hpres", root), head = $(".rx-hp__head", root);
    var t0 = 0, raf = 0, dur = 9000, winStart = 3200, winLen = 5000, clicked = [];
    function frame() { var t = performance.now() - t0; head.style.left = Math.min(100, t / dur * 100) + "%"; if (t < dur) raf = requestAnimationFrame(frame); else finish(); }
    function score(t) { if (t < winStart || t > winStart + winLen) return 0; return 5 - Math.floor((t - winStart) / (winLen / 5)); }
    function finish() {
      cancelAnimationFrame(raf); btn.disabled = false; click.disabled = true;
      if (clicked.length > 8) { res.innerHTML = "⚠️ <b>Score: 0.</b> Too many clicks in a rhythm — the real test flags this and gives zero for the clip."; return; }
      var best = clicked.reduce(function (m, t) { return Math.max(m, score(t)); }, 0);
      res.innerHTML = best ? "✅ You scored <b>" + best + " out of 5</b> on this hazard." + (best < 5 ? " Click as soon as you see it start to develop to score higher." : " Perfect timing!") : "❌ <b>0 points</b> — you clicked outside the scoring window. Click when the hazard <i>starts</i> to develop.";
    }
    btn.addEventListener("click", function () { clicked = []; res.textContent = ""; $$(".rx-hp__mark", root).forEach(function (m) { m.remove(); }); btn.disabled = true; click.disabled = false; t0 = performance.now(); frame(); click.focus(); });
    click.addEventListener("click", function () { var t = performance.now() - t0; clicked.push(t); var m = document.createElement("i"); m.className = "rx-hp__mark"; m.style.left = (t / dur * 100) + "%"; bar.appendChild(m); });
  }

  /* ---------- glossary filter ---------- */
  function glossary(root) {
    var input = $("input", root), items = $$("[data-term]", root), count = $(".js-gcount", root);
    input.addEventListener("input", function () {
      var q = input.value.toLowerCase().trim(), n = 0;
      items.forEach(function (it) { var on = !q || it.getAttribute("data-term").indexOf(q) > -1; it.hidden = !on; if (on) n++; });
      $$("[data-letter]", root).forEach(function (sec) { sec.hidden = !$$("[data-term]", sec).some(function (x) { return !x.hidden; }); });
      count.textContent = n + " term" + (n === 1 ? "" : "s");
    });
  }

  /* ---------- driving test feedback (goes to the DriveSQ admin) ---------- */
  function feedback(root) {
    var msg = $(".js-fbmsg", root), btn = $("button[type=submit]", root);
    root.addEventListener("submit", function (e) {
      e.preventDefault();
      var v = function (n) { var el = root.elements[n]; return el ? String(el.value || "").trim() : ""; };
      var name = v("fbname"), phone = v("fbphone"), result = v("fbresult"), text = v("fbtext");
      if (name.length < 2) { msg.textContent = "Please add your first name."; return; }
      if (!result) { msg.textContent = "Please choose how your test went."; return; }
      if (text.length < 15) { msg.textContent = "Please tell us a little more — at least a sentence."; return; }
      if (phone && window.SQ && SQ.phoneOk && !SQ.phoneOk(phone)) { msg.textContent = "That phone number doesn't look right — or leave it blank."; return; }
      if (!window.SQ || !SQ.sendBooking) { msg.textContent = "Sorry — please WhatsApp us your feedback instead."; return; }
      btn.disabled = true; msg.textContent = "Sending…";
      SQ.sendBooking({ source: "Driving test feedback", name: name, phone: phone, gearbox: v("fbgear"), message: text,
        lines: ["Test centre: " + root.getAttribute("data-centre"), "Result: " + result, v("fbwhen") ? "Test month: " + v("fbwhen") : "", v("fbfault") ? "Main fault/area: " + v("fbfault") : ""].filter(Boolean) })
        .then(function (ok) {
          btn.disabled = false;
          if (ok) { root.reset(); msg.innerHTML = "✅ <b>Thank you!</b> Your feedback reached the SQ Driving School team. We read every one and use it to keep this guide accurate."; }
          else msg.textContent = "Sorry — that didn't send. Please try again or WhatsApp us.";
        });
    });
  }

  function init() {
    $$("[data-rx=sun]").forEach(sun); $$("[data-rx=odds]").forEach(odds); $$("[data-rx=earn]").forEach(earn); $$("[data-rx=cite]").forEach(cite); $$("[data-rx=stop]").forEach(stopping); $$("[data-rx=testday]").forEach(testday); $$("[data-rx=timeline]").forEach(timeline); $$("[data-rx=hazard]").forEach(hazard); $$("[data-rx=glossary]").forEach(glossary); $$("form[data-rx=feedback]").forEach(feedback);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
