/* =========================================================
   SQ DRIVING SCHOOL — Core script
   A brand owned & managed by DriveSQ
   Crafted by Mohammed Qaim Abbas · sqwebsites.co.uk
   ========================================================= */
(function () {
  "use strict";

  /* ------------------------------------------------------
     CONFIG — edit prices, discounts and contact details here
     ------------------------------------------------------ */
  var SQ = (window.SQ = {
    phone: "07352 932003",
    phoneIntl: "+447352932003",
    wa: "447352932003",
    portalStudent: "https://www.drivesq.co.uk/student.html",
    portalInstructor: "https://www.drivesq.co.uk/portal.html",
    prices: {
      single: 40, // one-off 1 hour session
      hourly: 35, // standard rate (2 hour minimum)
      twoHour: 70, // standard 2 hour lesson
      block: 350, // 10 hour block
      blockDiscount: 320, // 10 hour block — NHS, students, M16/M18/M19
      blockHours: 10
    },
    offerPostcodes: ["M16", "M18", "M19"],
    // DVSA fees — check gov.uk for the latest
    dvsa: { theory: 23, practicalWeekday: 62, practicalEvening: 75 }
  });

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia && window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    sget: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    sset: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  };
  var gbp = function (n) { return "£" + Math.round(n).toLocaleString("en-GB"); };
  SQ.gbp = gbp;
  SQ.waLink = function (msg) { return "https://wa.me/" + SQ.wa + "?text=" + encodeURIComponent(msg); };

  /* ------------------------------------------------------
     THEME
     ------------------------------------------------------ */
  var savedTheme = store.get("sq-theme");
  if (savedTheme) document.documentElement.setAttribute("data-theme", savedTheme);
  function toggleTheme() {
    var next = document.documentElement.getAttribute("data-theme") === "light" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", next);
    store.set("sq-theme", next);
  }

  /* ------------------------------------------------------
     LANGUAGE (draft translations — have a native speaker check before relying on them)
     ------------------------------------------------------ */
  var I18N = {
    ur: {
      "nav.home": "ہوم", "nav.lessons": "اسباق", "nav.prices": "قیمتیں", "nav.discounts": "رعایتیں", "nav.tools": "ٹولز",
      "nav.portal": "اسٹوڈنٹ پورٹل", "nav.areas": "علاقے", "nav.contact": "رابطہ",
      "cta.book": "واٹس ایپ پر بک کریں", "cta.call": "کال کریں", "cta.prices": "قیمتیں دیکھیں",
      "hero.eyebrow": "گریٹر مانچسٹر · مینوئل اور آٹومیٹک",
      "hero.lead": "تیز، جدید اور پراعتماد ڈرائیونگ اسباق۔ DriveSQ کی طاقت سے — ہر طالب علم کے لیے مفت آن لائن اسٹوڈنٹ پورٹل کے ساتھ۔",
      "offer.title": "خصوصی پیشکش: M16، M18، M19 میں 10 گھنٹے صرف £320",
      "footer.owned": "SQ Driving School ایک برانڈ ہے جس کی ملکیت اور انتظام DriveSQ کے پاس ہے۔"
    },
    ar: {
      "nav.home": "الرئيسية", "nav.lessons": "الدروس", "nav.prices": "الأسعار", "nav.discounts": "الخصومات", "nav.tools": "الأدوات",
      "nav.portal": "بوابة الطالب", "nav.areas": "المناطق", "nav.contact": "اتصل بنا",
      "cta.book": "احجز عبر واتساب", "cta.call": "اتصل الآن", "cta.prices": "عرض الأسعار",
      "hero.eyebrow": "مانشستر الكبرى · يدوي وأوتوماتيك",
      "hero.lead": "دروس قيادة سريعة وعصرية وواثقة. بدعم من DriveSQ — مع بوابة طالب مجانية عبر الإنترنت لكل متعلم.",
      "offer.title": "عرض خاص: 10 ساعات مقابل 320 جنيهًا فقط في M16 وM18 وM19",
      "footer.owned": "SQ Driving School علامة تجارية مملوكة لشركة DriveSQ وتديرها."
    },
    pl: {
      "nav.home": "Start", "nav.lessons": "Lekcje", "nav.prices": "Cennik", "nav.discounts": "Zniżki", "nav.tools": "Narzędzia",
      "nav.portal": "Portal kursanta", "nav.areas": "Obszary", "nav.contact": "Kontakt",
      "cta.book": "Zarezerwuj przez WhatsApp", "cta.call": "Zadzwoń", "cta.prices": "Zobacz cennik",
      "hero.eyebrow": "Wielki Manchester · manual i automat",
      "hero.lead": "Szybkie, nowoczesne i pewne lekcje jazdy. Wspierane przez DriveSQ — z darmowym portalem online dla każdego kursanta.",
      "offer.title": "Oferta specjalna: 10 godzin za jedyne 320 £ w M16, M18 i M19",
      "footer.owned": "SQ Driving School to marka należąca do DriveSQ i przez nią zarządzana."
    }
  };
  var i18nOriginal = typeof WeakMap === "function" ? new WeakMap() : null;
  function applyLang(lang) {
    var dict = I18N[lang];
    $$("[data-i18n]").forEach(function (el) {
      if (!i18nOriginal) return;
      if (!i18nOriginal.has(el)) i18nOriginal.set(el, el.innerHTML);
      var key = el.getAttribute("data-i18n");
      el.innerHTML = dict && dict[key] ? dict[key] : i18nOriginal.get(el);
    });
    document.documentElement.lang = lang === "en" ? "en-GB" : lang;
    document.documentElement.dir = lang === "ur" || lang === "ar" ? "rtl" : "ltr";
    $$(".lang-select").forEach(function (s) { s.value = lang; });
    store.set("sq-lang", lang);
  }

  /* ------------------------------------------------------
     PRELOADER (once per session)
     ------------------------------------------------------ */
  function preloader() {
    var pl = $(".preloader");
    if (!pl) return;
    if (store.sget("sq-loaded") || reduceMotion) { pl.remove(); return; }
    document.body.classList.add("is-locked");
    var done = function () {
      pl.classList.add("is-done");
      document.body.classList.remove("is-locked");
      store.sset("sq-loaded", "1");
      setTimeout(function () { pl.remove(); }, 800);
    };
    setTimeout(done, 1700);
  }

  /* ------------------------------------------------------
     NAV
     ------------------------------------------------------ */
  function nav() {
    var navEl = $(".nav");
    var lastY = window.scrollY;
    var burger = $(".burger");
    var menu = $(".mobile-menu");
    window.addEventListener("scroll", function () {
      var y = window.scrollY;
      if (navEl) {
        navEl.classList.toggle("is-scrolled", y > 10);
        navEl.classList.toggle("is-hidden", y > 400 && y > lastY && !(menu && menu.classList.contains("is-open")));
      }
      lastY = y;
    }, { passive: true });
    if (burger && menu) {
      burger.addEventListener("click", function () {
        var open = burger.getAttribute("aria-expanded") !== "true";
        burger.setAttribute("aria-expanded", String(open));
        menu.classList.toggle("is-open", open);
        menu.setAttribute("aria-hidden", String(!open));
        document.body.classList.toggle("is-locked", open);
        $$("a", menu).forEach(function (a, i) { a.style.transitionDelay = open ? 0.15 + i * 0.04 + "s" : "0s"; });
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && menu.classList.contains("is-open")) burger.click();
      });
    }
    $$(".theme-toggle").forEach(function (b) { b.addEventListener("click", toggleTheme); });
    $$(".lang-select").forEach(function (s) { s.addEventListener("change", function () { applyLang(s.value); }); });
  }

  /* ------------------------------------------------------
     SCROLL PROGRESS + ROAD RAIL CAR
     ------------------------------------------------------ */
  function scrollFx() {
    var bar = $(".scroll-progress span");
    var car = $(".road-rail__car");
    var tFill = $(".timeline__fill");
    var timeline = $(".timeline");
    var steps = $$(".step");
    var ticking = false;
    function update() {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? window.scrollY / h : 0;
      if (bar) bar.style.width = p * 100 + "%";
      if (car) car.style.top = p * 100 + "%";
      if (timeline && tFill) {
        var r = timeline.getBoundingClientRect();
        var prog = Math.min(1, Math.max(0, (window.innerHeight * 0.6 - r.top) / r.height));
        tFill.style.height = prog * (r.height - 20) + "px";
        steps.forEach(function (s) {
          s.classList.toggle("is-active", s.getBoundingClientRect().top < window.innerHeight * 0.6);
        });
      }
      $$("[data-parallax]").forEach(function (el) {
        var speed = parseFloat(el.getAttribute("data-parallax")) || 0.2;
        var rect = el.parentElement.getBoundingClientRect();
        el.style.transform = "translate3d(0," + rect.top * -speed + "px,0)";
      });
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ------------------------------------------------------
     REVEAL + SPLIT CHARS + COUNTERS
     ------------------------------------------------------ */
  function splitChars() {
    $$("[data-split]").forEach(function (el) {
      var words = el.textContent.trim().split(/\s+/);
      el.innerHTML = "";
      el.classList.add("split-chars");
      var i = 0;
      words.forEach(function (w, wi) {
        var ws = document.createElement("span");
        ws.style.display = "inline-block";
        ws.style.whiteSpace = "nowrap";
        w.split("").forEach(function (ch) {
          var c = document.createElement("span");
          c.className = "char";
          c.textContent = ch;
          c.style.transitionDelay = i++ * 0.025 + "s";
          ws.appendChild(c);
        });
        el.appendChild(ws);
        if (wi < words.length - 1) el.appendChild(document.createTextNode(" "));
      });
      el.setAttribute("aria-label", words.join(" "));
    });
  }

  function countUp(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var dec = (el.getAttribute("data-count").split(".")[1] || "").length;
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduceMotion) { el.textContent = prefix + target.toFixed(dec) + suffix; return; }
    var start = null;
    var dur = 1800;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      var e = 1 - Math.pow(1 - p, 4);
      el.textContent = prefix + (target * e).toFixed(dec) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function reveal() {
    var els = $$("[data-reveal], .split-chars, [data-count], .phone, [data-gauge]");
    if (!("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        var d = el.getAttribute("data-delay");
        if (d) el.style.transitionDelay = d + "s";
        el.classList.add("is-in");
        if (el.hasAttribute("data-count")) countUp(el);
        if (el.hasAttribute("data-gauge")) animateGauge(el);
        io.unobserve(el);
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    els.forEach(function (el) { io.observe(el); });
    // stagger children
    $$("[data-stagger]").forEach(function (wrap) {
      var step = parseFloat(wrap.getAttribute("data-stagger")) || 0.08;
      $$("[data-reveal]", wrap).forEach(function (c, i) {
        if (!c.hasAttribute("data-delay")) c.setAttribute("data-delay", (i * step).toFixed(2));
      });
    });
  }

  /* ------------------------------------------------------
     GAUGE (speedometer)
     ------------------------------------------------------ */
  function animateGauge(el) {
    var val = parseFloat(el.getAttribute("data-gauge")) || 0;
    var arc = $(".gauge__arc", el);
    var needle = $(".gauge__needle", el);
    var num = $(".gauge__num", el);
    var len = arc ? arc.getTotalLength() : 0;
    if (arc) { arc.style.strokeDasharray = len; arc.style.strokeDashoffset = len; }
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / (reduceMotion ? 1 : 2200));
      var e = 1 - Math.pow(1 - p, 3);
      var v = val * e;
      if (arc) arc.style.strokeDashoffset = len - (len * v) / 100;
      if (needle) needle.setAttribute("transform", "rotate(" + (-120 + (240 * v) / 100) + " 160 160)");
      if (num) num.textContent = Math.round(v);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  SQ.setGauge = function (el, v) { el.setAttribute("data-gauge", v); animateGauge(el); };

  /* ------------------------------------------------------
     INTERACTIONS: tilt, glow, magnetic, ripple, cursor
     ------------------------------------------------------ */
  function interactions() {
    $$(".card, .tool, .price-card").forEach(function (card) {
      card.addEventListener("pointermove", function (e) {
        var r = card.getBoundingClientRect();
        card.style.setProperty("--mx", e.clientX - r.left + "px");
        card.style.setProperty("--my", e.clientY - r.top + "px");
      });
    });
    if (finePointer && !reduceMotion) {
      $$("[data-tilt]").forEach(function (el) {
        var max = parseFloat(el.getAttribute("data-tilt")) || 8;
        el.addEventListener("pointermove", function (e) {
          var r = el.getBoundingClientRect();
          var x = (e.clientX - r.left) / r.width - 0.5;
          var y = (e.clientY - r.top) / r.height - 0.5;
          el.style.transform = "perspective(900px) rotateY(" + x * max + "deg) rotateX(" + -y * max + "deg) translateZ(0)";
        });
        el.addEventListener("pointerleave", function () { el.style.transform = ""; });
      });
      $$(".btn, .icon-btn").forEach(function (b) {
        b.addEventListener("pointermove", function (e) {
          var r = b.getBoundingClientRect();
          var x = e.clientX - r.left - r.width / 2;
          var y = e.clientY - r.top - r.height / 2;
          b.style.transform = "translate(" + x * 0.18 + "px," + y * 0.25 + "px)";
        });
        b.addEventListener("pointerleave", function () { b.style.transform = ""; });
      });
      var glow = document.createElement("div");
      glow.className = "cursor-glow";
      var dot = document.createElement("div");
      dot.className = "cursor-dot";
      document.body.appendChild(glow);
      document.body.appendChild(dot);
      var gx = 0, gy = 0, tx = 0, ty = 0;
      window.addEventListener("pointermove", function (e) {
        tx = e.clientX; ty = e.clientY;
        dot.style.transform = "translate(" + (tx - 4) + "px," + (ty - 4) + "px)";
      });
      (function loop() {
        gx += (tx - gx) * 0.12; gy += (ty - gy) * 0.12;
        glow.style.transform = "translate(" + (gx - 210) + "px," + (gy - 210) + "px)";
        requestAnimationFrame(loop);
      })();
      document.addEventListener("pointerover", function (e) {
        dot.classList.toggle("is-hover", !!e.target.closest("a, button, label, input, select, textarea, [data-hover]"));
      });
      dot.style.left = "0"; dot.style.top = "0"; glow.style.left = "0"; glow.style.top = "0";
    }
    document.addEventListener("click", function (e) {
      var b = e.target.closest(".btn");
      if (!b || reduceMotion) return;
      var r = b.getBoundingClientRect();
      var s = document.createElement("span");
      var size = Math.max(r.width, r.height);
      s.className = "ripple";
      s.style.width = s.style.height = size + "px";
      s.style.left = e.clientX - r.left - size / 2 + "px";
      s.style.top = e.clientY - r.top - size / 2 + "px";
      b.appendChild(s);
      setTimeout(function () { s.remove(); }, 700);
    });
  }

  /* ------------------------------------------------------
     PAGE TRANSITIONS
     ------------------------------------------------------ */
  function transitions() {
    if (reduceMotion) return;
    var wipe = document.createElement("div");
    wipe.className = "page-wipe";
    document.body.appendChild(wipe);
    document.addEventListener("click", function (e) {
      var a = e.target.closest("a");
      if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || a.target === "_blank") return;
      var href = a.getAttribute("href");
      if (!href || href.charAt(0) === "#" || /^(https?:|mailto:|tel:|sms:)/.test(href) || a.hasAttribute("download")) return;
      e.preventDefault();
      wipe.classList.add("is-in");
      setTimeout(function () { window.location.href = href; }, 420);
    });
    window.addEventListener("pageshow", function () { wipe.classList.remove("is-in"); });
  }

  /* ------------------------------------------------------
     CANVAS FX — drifting red headlight particles + light streaks
     ------------------------------------------------------ */
  function canvasFx() {
    var c = $(".fx-canvas");
    if (!c || reduceMotion) return;
    var ctx = c.getContext("2d");
    var w, h, dpr = Math.min(2, window.devicePixelRatio || 1);
    var parts = [], streaks = [];
    function resize() {
      w = c.width = window.innerWidth * dpr;
      h = c.height = window.innerHeight * dpr;
      c.style.width = window.innerWidth + "px";
      c.style.height = window.innerHeight + "px";
      var n = Math.min(70, Math.floor(window.innerWidth / 22));
      parts = [];
      for (var i = 0; i < n; i++) parts.push({ x: Math.random() * w, y: Math.random() * h, r: (Math.random() * 1.8 + 0.4) * dpr, vx: (Math.random() - 0.5) * 0.15 * dpr, vy: -(Math.random() * 0.35 + 0.05) * dpr, a: Math.random() * 0.6 + 0.15 });
    }
    resize();
    window.addEventListener("resize", resize);
    var mouse = { x: -9999, y: -9999 };
    window.addEventListener("pointermove", function (e) { mouse.x = e.clientX * dpr; mouse.y = e.clientY * dpr; });
    var visible = true;
    document.addEventListener("visibilitychange", function () { visible = !document.hidden; });
    function frame() {
      requestAnimationFrame(frame);
      if (!visible) return;
      ctx.clearRect(0, 0, w, h);
      if (Math.random() < 0.02 && streaks.length < 4) {
        streaks.push({ x: -200 * dpr, y: Math.random() * h, len: (Math.random() * 200 + 120) * dpr, v: (Math.random() * 10 + 8) * dpr, a: Math.random() * 0.35 + 0.15 });
      }
      streaks = streaks.filter(function (s) {
        s.x += s.v;
        var g = ctx.createLinearGradient(s.x - s.len, s.y, s.x, s.y);
        g.addColorStop(0, "rgba(255,31,31,0)");
        g.addColorStop(1, "rgba(255,60,60," + s.a + ")");
        ctx.strokeStyle = g;
        ctx.lineWidth = 1.5 * dpr;
        ctx.beginPath(); ctx.moveTo(s.x - s.len, s.y); ctx.lineTo(s.x, s.y); ctx.stroke();
        return s.x - s.len < w;
      });
      parts.forEach(function (p) {
        var dx = p.x - mouse.x, dy = p.y - mouse.y, d = Math.sqrt(dx * dx + dy * dy);
        if (d < 120 * dpr) { p.x += (dx / d) * 1.2; p.y += (dy / d) * 1.2; }
        p.x += p.vx; p.y += p.vy;
        if (p.y < -10) { p.y = h + 10; p.x = Math.random() * w; }
        if (p.x < -10) p.x = w + 10; if (p.x > w + 10) p.x = -10;
        ctx.beginPath();
        ctx.fillStyle = "rgba(255,40,40," + p.a + ")";
        ctx.shadowBlur = 12 * dpr; ctx.shadowColor = "rgba(255,31,31,0.9)";
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
      });
      ctx.shadowBlur = 0;
    }
    frame();
  }

  function speedLines() {
    $$(".speed-lines").forEach(function (wrap) {
      if (reduceMotion) return;
      for (var i = 0; i < 14; i++) {
        var l = document.createElement("i");
        l.style.top = Math.random() * 100 + "%";
        l.style.animationDuration = Math.random() * 2.5 + 1.5 + "s";
        l.style.animationDelay = Math.random() * 4 + "s";
        l.style.width = Math.random() * 25 + 10 + "%";
        wrap.appendChild(l);
      }
    });
  }

  function typewriter() {
    $$("[data-type]").forEach(function (el) {
      var words = el.getAttribute("data-type").split("|");
      if (reduceMotion) { el.textContent = words[0]; return; }
      var wi = 0, ci = 0, del = false;
      el.classList.add("type-cursor");
      (function tick() {
        var word = words[wi];
        el.textContent = word.slice(0, ci);
        if (!del && ci < word.length) { ci++; setTimeout(tick, 70); }
        else if (!del) { del = true; setTimeout(tick, 1800); }
        else if (ci > 0) { ci--; setTimeout(tick, 35); }
        else { del = false; wi = (wi + 1) % words.length; setTimeout(tick, 300); }
      })();
    });
  }

  SQ.confetti = function () {
    if (reduceMotion) return;
    var colors = ["#ff1f1f", "#ffffff", "#ff4d4d", "#8a0000", "#22e07a"];
    for (var i = 0; i < 120; i++) {
      var c = document.createElement("i");
      c.className = "confetti";
      c.style.left = Math.random() * 100 + "vw";
      c.style.background = colors[i % colors.length];
      c.style.animationDuration = Math.random() * 2 + 2 + "s";
      c.style.animationDelay = Math.random() * 0.6 + "s";
      c.style.transform = "rotate(" + Math.random() * 360 + "deg)";
      document.body.appendChild(c);
      setTimeout(function (el) { return function () { el.remove(); }; }(c), 5000);
    }
  };

  /* ------------------------------------------------------
     POSTCODE DATA — Greater Manchester outward codes
     ------------------------------------------------------ */
  var B = { MAN: "Manchester", SAL: "Salford", TRA: "Trafford", STO: "Stockport", TAM: "Tameside", OLD: "Oldham", ROC: "Rochdale", BUR: "Bury", BOL: "Bolton", WIG: "Wigan" };
  var PC = {
    M1: [B.MAN, "City Centre"], M2: [B.MAN, "City Centre"], M3: [B.MAN, "Deansgate / Salford"], M4: [B.MAN, "Ancoats / Northern Quarter"],
    M5: [B.SAL, "Ordsall / Seedley"], M6: [B.SAL, "Pendleton / Weaste"], M7: [B.SAL, "Broughton / Kersal"], M8: [B.MAN, "Cheetham Hill / Crumpsall"],
    M9: [B.MAN, "Blackley / Harpurhey"], M11: [B.MAN, "Openshaw / Clayton"], M12: [B.MAN, "Longsight / Ardwick"], M13: [B.MAN, "Ardwick / Victoria Park"],
    M14: [B.MAN, "Fallowfield / Moss Side / Rusholme"], M15: [B.MAN, "Hulme"], M16: [B.MAN, "Old Trafford / Whalley Range / Firswood"],
    M17: [B.TRA, "Trafford Park"], M18: [B.MAN, "Gorton / Abbey Hey"], M19: [B.MAN, "Levenshulme / Burnage"], M20: [B.MAN, "Didsbury / Withington"],
    M21: [B.MAN, "Chorlton-cum-Hardy"], M22: [B.MAN, "Wythenshawe / Northenden"], M23: [B.MAN, "Baguley / Brooklands"], M24: [B.ROC, "Middleton"],
    M25: [B.BUR, "Prestwich"], M26: [B.BUR, "Radcliffe"], M27: [B.SAL, "Swinton / Pendlebury"], M28: [B.SAL, "Worsley / Walkden"],
    M29: [B.WIG, "Tyldesley / Astley"], M30: [B.SAL, "Eccles"], M31: [B.TRA, "Partington / Carrington"], M32: [B.TRA, "Stretford"],
    M33: [B.TRA, "Sale"], M34: [B.TAM, "Denton / Audenshaw"], M35: [B.OLD, "Failsworth"], M38: [B.SAL, "Little Hulton"],
    M40: [B.MAN, "Newton Heath / Moston"], M41: [B.TRA, "Urmston / Flixton"], M43: [B.TAM, "Droylsden"], M44: [B.SAL, "Irlam / Cadishead"],
    M45: [B.BUR, "Whitefield"], M46: [B.WIG, "Atherton"], M50: [B.SAL, "Salford Quays"], M90: [B.MAN, "Manchester Airport"],
    BL0: [B.BUR, "Ramsbottom"], BL1: [B.BOL, "Bolton North"], BL2: [B.BOL, "Bolton East"], BL3: [B.BOL, "Bolton South"],
    BL4: [B.BOL, "Farnworth / Kearsley"], BL5: [B.BOL, "Westhoughton"], BL6: [B.BOL, "Horwich / Blackrod"], BL7: [B.BOL, "Bromley Cross / Egerton"],
    BL8: [B.BUR, "Tottington / Bury West"], BL9: [B.BUR, "Bury"],
    OL1: [B.OLD, "Oldham Centre"], OL2: [B.OLD, "Royton / Shaw"], OL3: [B.OLD, "Saddleworth"], OL4: [B.OLD, "Lees / Springhead"],
    OL5: [B.TAM, "Mossley"], OL6: [B.TAM, "Ashton-under-Lyne"], OL7: [B.TAM, "Ashton West"], OL8: [B.OLD, "Hollinwood / Fitton Hill"],
    OL9: [B.OLD, "Chadderton"], OL10: [B.ROC, "Heywood"], OL11: [B.ROC, "Rochdale South"], OL12: [B.ROC, "Rochdale North / Whitworth"],
    OL15: [B.ROC, "Littleborough"], OL16: [B.ROC, "Rochdale East / Milnrow"],
    SK1: [B.STO, "Stockport Centre"], SK2: [B.STO, "Offerton"], SK3: [B.STO, "Edgeley / Cheadle Heath"], SK4: [B.STO, "Heaton Moor / Heaton Chapel"],
    SK5: [B.STO, "Reddish / Brinnington"], SK6: [B.STO, "Marple / Bredbury / Romiley"], SK7: [B.STO, "Bramhall / Hazel Grove"], SK8: [B.STO, "Cheadle / Gatley"],
    SK14: [B.TAM, "Hyde"], SK15: [B.TAM, "Stalybridge"], SK16: [B.TAM, "Dukinfield"],
    WA14: [B.TRA, "Altrincham"], WA15: [B.TRA, "Hale / Timperley"],
    WN1: [B.WIG, "Wigan Centre"], WN2: [B.WIG, "Hindley / Ince"], WN3: [B.WIG, "Wigan South"], WN4: [B.WIG, "Ashton-in-Makerfield"],
    WN5: [B.WIG, "Orrell / Pemberton"], WN6: [B.WIG, "Standish / Shevington"], WN7: [B.WIG, "Leigh"]
  };
  var PARTIAL = { WA3: "Golborne / Lowton (Wigan)", WN8: "Upholland", SK12: "Poynton / Disley", SK9: "Wilmslow", OL13: "Bacup", OL14: "Todmorden", WA13: "Lymm" };
  SQ.postcodes = PC;
  SQ.checkPostcode = function (raw) {
    var s = String(raw || "").toUpperCase().replace(/[^A-Z0-9]/g, "");
    if (!s) return { status: "empty" };
    var outward = s;
    if (s.length >= 5) outward = s.slice(0, s.length - 3); // strip inward code (e.g. 4AB)
    if (!/^[A-Z]{1,2}[0-9][0-9A-Z]?$/.test(outward)) return { status: "invalid" };
    if (PC[outward]) {
      return { status: "covered", outward: outward, borough: PC[outward][0], area: PC[outward][1], offer: SQ.offerPostcodes.indexOf(outward) > -1 };
    }
    if (PARTIAL[outward]) return { status: "partial", outward: outward, area: PARTIAL[outward] };
    return { status: "outside", outward: outward };
  };

  /* ------------------------------------------------------
     PRICE ENGINE
     ------------------------------------------------------ */
  SQ.quote = function (hours, discounted) {
    var P = SQ.prices;
    if (hours === 1) return { total: P.single, standard: P.single, save: 0, blocks: 0, rest: 1, single: true };
    var blocks = Math.floor(hours / P.blockHours);
    var rest = hours - blocks * P.blockHours;
    var blockPrice = discounted ? P.blockDiscount : P.block;
    var total = blocks * blockPrice + rest * P.hourly;
    var standard = hours * P.hourly;
    return { total: total, standard: standard, save: standard - total, blocks: blocks, rest: rest, blockPrice: blockPrice };
  };

  /* ------------------------------------------------------
     TOOL: Postcode checker
     ------------------------------------------------------ */
  function toolPostcode() {
    $$("[data-tool='postcode']").forEach(function (form) {
      var input = $("input", form);
      var out = $(".result", form.parentElement) || $(".result", form);
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var r = SQ.checkPostcode(input.value);
        out.className = "result is-visible";
        if (r.status === "empty" || r.status === "invalid") {
          out.classList.add("result--warn");
          out.innerHTML = "<b>Hmm, that doesn't look like a UK postcode.</b><p class='mb-0'>Try something like <span class='mono'>M19 2AB</span> or just <span class='mono'>M19</span>.</p>";
        } else if (r.status === "covered" && r.offer) {
          out.classList.add("result--offer");
          out.innerHTML = "<span class='tag'>SPECIAL OFFER UNLOCKED</span><div class='result__big glow-text'>10 hours for " + gbp(SQ.prices.blockDiscount) + "</div>" +
            "<p><b>" + r.outward + "</b> · " + r.area + " (" + r.borough + ") is in our special offer zone. You save " + gbp(SQ.prices.block - SQ.prices.blockDiscount) + " on a 10 hour block.</p>" +
            "<a class='btn btn--red' target='_blank' rel='noopener' href='" + SQ.waLink("Hi SQ Driving School! My postcode is " + r.outward + " — I'd like the 10 hours for £" + SQ.prices.blockDiscount + " special offer.") + "'>Claim on WhatsApp</a>";
          SQ.confetti();
        } else if (r.status === "covered") {
          out.classList.add("result--ok");
          out.innerHTML = "<span class='tag tag--green'>WE COVER YOU ✓</span><div class='result__big'>" + r.outward + " · " + r.borough + "</div>" +
            "<p>Great news — we teach in <b>" + r.area + "</b>. Lessons from " + gbp(SQ.prices.twoHour) + " for 2 hours, or a 10 hour block for " + gbp(SQ.prices.block) + ".</p>" +
            "<a class='btn btn--red' target='_blank' rel='noopener' href='" + SQ.waLink("Hi SQ Driving School! My postcode is " + r.outward + " (" + r.area + "). I'd like to book lessons.") + "'>Book on WhatsApp</a>";
        } else if (r.status === "partial") {
          out.classList.add("result--warn");
          out.innerHTML = "<span class='tag'>ASK US</span><div class='result__big'>" + r.outward + "</div><p>" + r.area + " sits on the edge of Greater Manchester. Message us and we'll confirm whether an instructor can reach you.</p>" +
            "<a class='btn btn--wa' target='_blank' rel='noopener' href='" + SQ.waLink("Hi! Do you cover postcode " + r.outward + "?") + "'>Ask on WhatsApp</a>";
        } else {
          out.classList.add("result--bad");
          out.innerHTML = "<span class='tag'>OUTSIDE AREA</span><div class='result__big'>" + r.outward + "</div><p>That postcode is outside Greater Manchester. If you can get to a Manchester pick-up point, message us and we'll see what we can do.</p>";
        }
      });
    });
  }

  /* ------------------------------------------------------
     TOOL: Area / town finder
     ------------------------------------------------------ */
  function toolArea() {
    $$("[data-tool='area']").forEach(function (form) {
      var input = $("input", form);
      var out = $(".result", form);
      var list = $("datalist", form);
      var towns = [];
      Object.keys(PC).forEach(function (k) {
        PC[k][1].split(" / ").forEach(function (t) { towns.push({ t: t, k: k, b: PC[k][0] }); });
      });
      if (list) towns.forEach(function (x) { var o = document.createElement("option"); o.value = x.t; list.appendChild(o); });
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var q = input.value.trim().toLowerCase();
        var hit = towns.filter(function (x) { return x.t.toLowerCase().indexOf(q) > -1 || x.b.toLowerCase() === q; });
        out.className = "result is-visible";
        if (!q || !hit.length) {
          out.classList.add("result--warn");
          out.innerHTML = "<b>We couldn't find that area.</b><p class='mb-0'>We cover all 10 Greater Manchester boroughs — try your postcode in the checker instead, or WhatsApp us.</p>";
          return;
        }
        out.classList.add("result--ok");
        var codes = hit.slice(0, 12).map(function (x) { return "<span class='pc" + (SQ.offerPostcodes.indexOf(x.k) > -1 ? " pc--hot" : "") + "'>" + x.k + " · " + x.t + "</span>"; }).join(" ");
        out.innerHTML = "<span class='tag tag--green'>COVERED ✓</span><p class='mt-1'>Yes, we teach in <b>" + hit[0].t + "</b> (" + hit[0].b + ").</p><div class='pc-cloud'>" + codes + "</div>";
      });
    });
  }

  /* ------------------------------------------------------
     TOOL: Package / price builder
     ------------------------------------------------------ */
  function toolBuilder() {
    $$("[data-tool='builder']").forEach(function (root) {
      var range = $("[name='hours']", root);
      var hoursOut = $(".js-hours", root);
      var table = $(".js-summary", root);
      var totalBig = $(".js-total", root);
      var waBtn = $(".js-wa", root);
      function val(name) { var el = $("[name='" + name + "']:checked", root); return el ? el.value : ""; }
      function update() {
        var single = val("type") === "single";
        range.disabled = single;
        var hours = single ? 1 : parseInt(range.value, 10);
        var addOns = $$("[name='addon']:checked", root);
        var addHours = single ? 0 : addOns.reduce(function (s, a) { return s + parseInt(a.getAttribute("data-hours"), 10); }, 0);
        var totalHours = hours + addHours;
        var disc = val("discount");
        var discounted = disc && disc !== "none";
        var q = SQ.quote(totalHours, discounted && !single);
        range.style.setProperty("--p", ((range.value - range.min) / (range.max - range.min)) * 100 + "%");
        hoursOut.textContent = single ? "1 hour (single session)" : hours + " hours";
        var rows = [];
        if (q.single) rows.push(["Single 1 hour session", gbp(SQ.prices.single)]);
        else {
          if (q.blocks) rows.push([q.blocks + " × 10 hour block" + (discounted ? " (" + $("[name='discount']:checked", root).getAttribute("data-label") + ")" : ""), gbp(q.blocks * q.blockPrice)]);
          if (q.rest) rows.push([q.rest + " extra hours × " + gbp(SQ.prices.hourly), gbp(q.rest * SQ.prices.hourly)]);
          addOns.forEach(function (a) { rows.push(["incl. " + a.getAttribute("data-label") + " (" + a.getAttribute("data-hours") + " hrs)", "✓"]); });
        }
        var html = rows.map(function (r) { return "<tr><td>" + r[0] + "</td><td>" + r[1] + "</td></tr>"; }).join("");
        if (q.save > 0) html += "<tr class='save'><td>You save</td><td>−" + gbp(q.save) + "</td></tr>";
        html += "<tr class='total'><td>Total · " + totalHours + " hr" + (totalHours > 1 ? "s" : "") + "</td><td>" + gbp(q.total) + "</td></tr>";
        table.innerHTML = html;
        totalBig.textContent = gbp(q.total);
        totalBig.classList.remove("bump"); void totalBig.offsetWidth; totalBig.classList.add("bump");
        var msg = "Hi SQ Driving School! I built a package on your website:\n• " + val("trans") + " lessons\n• " + totalHours + " hours" +
          (addOns.length ? "\n• Includes: " + addOns.map(function (a) { return a.getAttribute("data-label"); }).join(", ") : "") +
          (discounted ? "\n• Discount: " + $("[name='discount']:checked", root).getAttribute("data-label") : "") +
          "\n• Quoted total: " + gbp(q.total) + "\nCan I book this?";
        waBtn.href = SQ.waLink(msg);
      }
      root.addEventListener("input", update);
      root.addEventListener("change", update);
      update();
    });
  }

  /* ------------------------------------------------------
     TOOL: How many lessons do I need?
     ------------------------------------------------------ */
  function toolLessons() {
    $$("[data-tool='lessons']").forEach(function (form) {
      var out = $(".result", form);
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var fd = new FormData(form);
        var base = { none: 45, some: 32, lots: 20, failed: 12, abroad: 10 }[fd.get("exp")] || 40;
        var mult = { nervous: 1.15, ok: 1, confident: 0.9 }[fd.get("conf")] || 1;
        if (fd.get("trans") === "Automatic") mult *= 0.85;
        if (fd.get("practice") === "yes") mult *= 0.85;
        var hrs = Math.max(6, Math.round((base * mult) / 2) * 2);
        var low = Math.max(4, hrs - 6), high = hrs + 6;
        var std = SQ.quote(hrs, false).total;
        var dsc = SQ.quote(hrs, true).total;
        var weekly = parseInt(fd.get("pace"), 10) || 4;
        var weeks = Math.ceil(hrs / weekly);
        out.className = "result is-visible result--ok";
        out.innerHTML = "<span class='tag tag--green'>YOUR ESTIMATE</span><div class='result__big'><span class='glow-text'>" + low + "–" + high + "</span> hours</div>" +
          "<table class='summary'><tr><td>Most likely</td><td>" + hrs + " hrs</td></tr><tr><td>Standard price</td><td>" + gbp(std) + "</td></tr>" +
          "<tr class='save'><td>With NHS / student / M16·M18·M19 offer</td><td>" + gbp(dsc) + "</td></tr><tr><td>At " + weekly + " hrs per week</td><td>≈ " + weeks + " weeks</td></tr></table>" +
          "<p class='note'>An estimate only, based on your answers. The DVSA says learners typically need around 45 hours of lessons plus 22 hours of private practice. Your instructor will give you a personal plan after your first lesson.</p>" +
          "<a class='btn btn--red' target='_blank' rel='noopener' href='" + SQ.waLink("Hi! The lesson calculator says I need about " + hrs + " hours of " + fd.get("trans") + " lessons. Can I book?") + "'>Book this plan</a>";
      });
    });
  }

  /* ------------------------------------------------------
     TOOL: Test readiness checker
     ------------------------------------------------------ */
  function toolReadiness() {
    $$("[data-tool='readiness']").forEach(function (root) {
      var boxes = $$("input[type='checkbox']", root);
      var bar = $(".progress span", root);
      var pct = $(".js-pct", root);
      var msg = $(".js-msg", root);
      var gauge = $("[data-gauge]", root);
      function update() {
        var n = boxes.filter(function (b) { return b.checked; }).length;
        var p = Math.round((n / boxes.length) * 100);
        bar.style.width = p + "%";
        pct.textContent = p + "%";
        if (gauge) SQ.setGauge(gauge, p);
        msg.textContent = p === 100 ? "You're test ready! Book a mock test with us to make sure." :
          p >= 75 ? "Nearly there — a couple more skills to polish." :
          p >= 40 ? "Good progress. Keep building those skills." : "Early days — every expert was once a beginner.";
        if (p === 100 && !root.dataset.done) { root.dataset.done = "1"; SQ.confetti(); }
        if (p < 100) delete root.dataset.done;
      }
      boxes.forEach(function (b) { b.addEventListener("change", update); });
    });
  }

  /* ------------------------------------------------------
     TOOL: Test countdown / planner
     ------------------------------------------------------ */
  function toolCountdown() {
    $$("[data-tool='countdown']").forEach(function (form) {
      var out = $(".result", form);
      var date = $("input[type='date']", form);
      try { date.min = new Date().toISOString().slice(0, 10); } catch (e) {}
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var d = new Date(date.value + "T09:00:00");
        var have = parseInt($("[name='done']", form).value, 10) || 0;
        var need = parseInt($("[name='need']", form).value, 10) || 40;
        var days = Math.ceil((d - new Date()) / 86400000);
        out.className = "result is-visible";
        if (!date.value || isNaN(days) || days < 1) { out.classList.add("result--warn"); out.innerHTML = "Pick a test date in the future."; return; }
        var weeks = Math.max(1, days / 7);
        var left = Math.max(0, need - have);
        var perWeek = Math.ceil(left / weeks);
        out.classList.add(perWeek > 10 ? "result--warn" : "result--ok");
        out.innerHTML = "<div class='result__big'><span class='glow-text'>" + days + "</span> days to go</div>" +
          "<table class='summary'><tr><td>Hours still needed</td><td>" + left + "</td></tr><tr><td>Weeks left</td><td>" + weeks.toFixed(1) + "</td></tr><tr><td>Suggested pace</td><td>" + perWeek + " hrs / week</td></tr></table>" +
          (perWeek > 10 ? "<p>That's a fast pace — our intensive courses are built for exactly this.</p><a class='btn btn--red' href='intensive.html'>See intensive courses</a>" :
          "<a class='btn btn--red' target='_blank' rel='noopener' href='" + SQ.waLink("Hi! My test is in " + days + " days and I need about " + left + " more hours. Can you fit me in?") + "'>Plan my lessons</a>");
      });
    });
  }

  /* ------------------------------------------------------
     TOOL: Total budget calculator (lessons + DVSA fees)
     ------------------------------------------------------ */
  function toolBudget() {
    $$("[data-tool='budget']").forEach(function (root) {
      var out = $(".js-budget", root);
      function update() {
        var hrs = parseInt($("[name='bhours']", root).value, 10) || 0;
        var disc = $("[name='bdisc']", root).checked;
        var evening = $("[name='bslot']", root).checked;
        var theoryDone = $("[name='btheory']", root).checked;
        var q = SQ.quote(hrs, disc);
        var practical = evening ? SQ.dvsa.practicalEvening : SQ.dvsa.practicalWeekday;
        var theory = theoryDone ? 0 : SQ.dvsa.theory;
        var total = q.total + practical + theory;
        out.innerHTML = "<tr><td>" + hrs + " hrs of lessons</td><td>" + gbp(q.total) + "</td></tr><tr><td>Theory test (DVSA)</td><td>" + (theoryDone ? "done" : gbp(theory)) + "</td></tr>" +
          "<tr><td>Practical test (DVSA" + (evening ? ", evening/weekend" : ", weekday") + ")</td><td>" + gbp(practical) + "</td></tr><tr class='total'><td>Estimated total</td><td>" + gbp(total) + "</td></tr>";
      }
      root.addEventListener("input", update);
      update();
    });
  }

  /* ------------------------------------------------------
     TOOL: Intensive course planner
     ------------------------------------------------------ */
  function toolIntensive() {
    $$("[data-tool='intensive']").forEach(function (root) {
      var out = $(".js-plan", root);
      function val(n) { var el = $("[name='" + n + "']:checked", root); return el ? el.value : ""; }
      function update() {
        var hrs = parseInt(val("ihours"), 10);
        var wks = parseInt(val("iweeks"), 10);
        var days = wks * 5;
        var perDay = (hrs / days).toFixed(1);
        var q = SQ.quote(hrs, val("idisc") === "yes");
        out.innerHTML = "<table class='summary'><tr><td>Course length</td><td>" + hrs + " hrs over " + wks + " week" + (wks > 1 ? "s" : "") + "</td></tr>" +
          "<tr><td>Driving days</td><td>" + days + " (Mon–Fri)</td></tr><tr><td>Average per day</td><td>" + perDay + " hrs</td></tr>" +
          "<tr class='total'><td>Lesson cost</td><td>" + gbp(q.total) + "</td></tr></table>" +
          "<a class='btn btn--red btn--block' target='_blank' rel='noopener' href='" + SQ.waLink("Hi! I'm interested in a " + hrs + " hour intensive course over " + wks + " week(s).") + "'>Request this course</a>";
      }
      root.addEventListener("change", update);
      update();
    });
  }

  /* ------------------------------------------------------
     CONTACT FORM → WhatsApp
     ------------------------------------------------------ */
  function contactForm() {
    $$("[data-tool='contact']").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var fd = new FormData(form);
        var lines = ["Hi SQ Driving School! New enquiry from your website:"];
        fd.forEach(function (v, k) { if (String(v).trim()) lines.push("• " + k + ": " + v); });
        window.open(SQ.waLink(lines.join("\n")), "_blank", "noopener");
      });
    });
  }

  /* ------------------------------------------------------
     THEORY QUIZ
     ------------------------------------------------------ */
  var QUESTIONS = [
    ["What is the typical overall stopping distance for a car at 30mph on a dry road?", ["12 metres", "23 metres", "36 metres", "53 metres"], 1, "At 30mph: 9m thinking + 14m braking = 23m — about six car lengths."],
    ["What is the typical overall stopping distance at 70mph on a dry road?", ["53 metres", "73 metres", "96 metres", "120 metres"], 2, "At 70mph: 21m thinking + 75m braking = 96m."],
    ["How much can stopping distances increase on icy roads?", ["Up to double", "Up to five times", "Up to ten times", "They don't change"], 2, "On ice, braking distances can be up to ten times greater than on a dry road."],
    ["On wet roads, stopping distances will be at least…", ["The same", "Double", "Triple", "Half"], 1, "Allow at least double the separation distance in the wet."],
    ["What is the legal minimum tread depth for car tyres?", ["1mm", "1.6mm", "2mm", "3mm"], 1, "1.6mm across the central three-quarters of the tread, around the entire circumference."],
    ["What is the national speed limit for cars on a single carriageway road?", ["50mph", "60mph", "70mph", "40mph"], 1, "60mph on single carriageways, 70mph on dual carriageways and motorways."],
    ["What is the national speed limit for cars on a dual carriageway?", ["60mph", "65mph", "70mph", "80mph"], 2, "70mph for cars and motorcycles on dual carriageways."],
    ["In good dry conditions, what time gap should you leave behind the vehicle in front?", ["At least one second", "At least two seconds", "At least five seconds", "At least ten seconds"], 1, "The two-second rule — and at least double that in the wet."],
    ["What do circular road signs mainly do?", ["Warn", "Give orders", "Give directions", "Show tourist information"], 1, "Circles give orders, triangles warn, rectangles inform."],
    ["A road sign with a red circle generally means…", ["A positive instruction", "Something is prohibited", "A warning", "Tourist information"], 1, "Red circles are prohibitive — they tell you what you must NOT do."],
    ["Most blue circular signs mean…", ["A positive (mandatory) instruction", "A prohibition", "A warning", "Motorway information"], 0, "Blue circles give a mandatory instruction, such as 'turn left' or 'minimum speed'."],
    ["What does a flashing amber light at a pelican crossing mean?", ["Stop and wait", "Give way to pedestrians on the crossing; go if it's clear", "Speed up to clear the crossing", "The lights are faulty"], 1, "You must give way to any pedestrians still on the crossing."],
    ["At a mini-roundabout you should normally give way to traffic from…", ["The left", "The right", "Straight ahead", "No one"], 1, "Give way to traffic approaching from your right, unless signs say otherwise."],
    ["When may you enter a yellow box junction?", ["Whenever the lights are green", "Only when your exit road or lane is clear", "Only at night", "Never"], 1, "Don't enter unless your exit is clear — except when turning right and only blocked by oncoming traffic or other vehicles waiting to turn right."],
    ["What is the penalty for using a hand-held phone while driving?", ["3 points and £100", "6 points and £200", "No points, £50 fine", "A warning only"], 1, "6 penalty points and a £200 fine — and a new driver could lose their licence."],
    ["Within two years of passing, your licence is revoked if you get…", ["3 or more points", "6 or more points", "9 or more points", "12 or more points"], 1, "New drivers who reach 6 points in their first two years lose their licence."],
    ["Who is legally responsible for making sure a child under 14 wears a seat belt?", ["The child", "The parent, even if not in the car", "The driver", "No one"], 2, "The driver is responsible for passengers under 14."],
    ["When overtaking a cyclist at speeds up to 30mph, leave at least…", ["0.5 metres", "1 metre", "1.5 metres", "3 metres"], 2, "The Highway Code recommends at least 1.5 metres at speeds up to 30mph, and more at higher speeds."],
    ["Under the hierarchy of road users, who carries the greatest responsibility?", ["Pedestrians", "Cyclists", "Those who can cause the greatest harm", "Whoever is going fastest"], 2, "Those driving larger, heavier vehicles carry the greatest responsibility to reduce danger to others."],
    ["You're turning left into a side road and a pedestrian is waiting to cross it. You should…", ["Carry on — you have priority", "Give way to the pedestrian", "Sound your horn", "Flash your lights"], 1, "Rule H2: give way to pedestrians crossing or waiting to cross a road you're turning into."],
    ["When should you use front or rear fog lights?", ["Whenever it rains", "When visibility is seriously reduced — generally under 100 metres", "At night on unlit roads", "On motorways only"], 1, "Use them when visibility drops below about 100 metres — and switch them off when it improves."],
    ["What does the routine 'MSM' stand for?", ["Move, Steer, Manoeuvre", "Mirror, Signal, Manoeuvre", "Mirror, Speed, Move", "Mind, See, Move"], 1, "Mirror – Signal – Manoeuvre (often taught as MSPSL: Mirror, Signal, Position, Speed, Look)."],
    ["Coasting (driving with the clutch down or in neutral) is dangerous because…", ["It uses more fuel", "It reduces your control of the car", "It damages the tyres", "It's not dangerous"], 1, "Coasting reduces engine braking and steering control."],
    ["When must you not use your horn in a built-up area while moving?", ["Between 11:30pm and 7am", "Between 9pm and 6am", "On Sundays", "Never — it's always allowed"], 0, "Don't use your horn between 11:30pm and 7am in a built-up area, unless another road user poses a danger."],
    ["What do the zig-zag lines at a zebra crossing mean?", ["You may park briefly", "No parking or overtaking", "Buses only", "Slow down to 10mph"], 1, "You must not park, wait or overtake the leading vehicle on the zig-zag lines."],
    ["An ambulance with blue lights is behind you at a red traffic light. You should…", ["Go through the red light", "Stay calm and wait — don't break the law to let it pass", "Mount the kerb", "Brake sharply"], 1, "Don't put yourself or others at risk or break the law — move over only when it's safe and legal."],
    ["When should you check your tyre pressures?", ["After a long journey", "When the tyres are cold", "Only at your MOT", "When the tyres are hot"], 1, "Check them cold for an accurate reading."],
    ["What is the pass mark for the multiple-choice part of the car theory test?", ["35 out of 50", "40 out of 50", "43 out of 50", "50 out of 50"], 2, "You need 43/50 on the multiple choice, plus 44/75 on hazard perception."],
    ["How many driving faults (minors) can you get and still pass your practical test?", ["Up to 5", "Up to 10", "Up to 15", "Up to 20"], 2, "Up to 15 driving faults — but any serious or dangerous fault is an automatic fail."],
    ["Can learner drivers have lessons on motorways?", ["Never", "Yes, with an approved instructor in a dual-controlled car", "Yes, with any adult over 21", "Only at night"], 1, "Since 2018 learners can drive on motorways with an ADI in a car fitted with dual controls."],
    ["Double white lines where the line nearest you is solid mean…", ["You may overtake if it's clear", "You must not cross or straddle it, except in certain situations", "Parking is allowed", "It's a bus lane"], 1, "You may only cross to turn, enter premises, pass a stationary vehicle, or overtake a cyclist/horse going 10mph or less."],
    ["Red lights are flashing at a level crossing. You must…", ["Speed up and cross quickly", "Stop", "Cross if you can't see a train", "Sound your horn and continue"], 1, "Flashing red lights mean STOP — a train is approaching."],
    ["You must never place a rear-facing baby seat…", ["In the back seat", "In front of an active passenger airbag", "Behind the driver", "In an estate car"], 1, "An inflating airbag could cause serious injury. Deactivate it or use the back seat."],
    ["How long does the practical car driving test take?", ["About 15 minutes", "About 40 minutes", "About 90 minutes", "Two hours"], 1, "Around 40 minutes, including about 20 minutes of independent driving."],
    ["What is the drink-drive limit in England (blood)?", ["50mg per 100ml", "80mg per 100ml", "100mg per 100ml", "There is no limit"], 1, "80mg of alcohol per 100ml of blood in England and Wales. The safest limit is none at all."],
    ["Parking on a road at night with a speed limit over 30mph, you must…", ["Switch on parking lights", "Use hazard lights", "Leave headlights on full beam", "Nothing"], 0, "Cars must display parking lights on roads with a speed limit greater than 30mph."],
    ["What should you do if you feel tired while driving on a motorway?", ["Open the window and carry on", "Leave at the next exit or services and rest", "Stop on the hard shoulder", "Speed up to get home sooner"], 1, "Stop somewhere safe. Never use the hard shoulder to rest."],
    ["A triangular road sign usually…", ["Gives an order", "Gives a warning", "Gives directions", "Shows parking rules"], 1, "Triangles warn of hazards ahead."],
    ["You may use hazard warning lights while moving to…", ["Thank another driver", "Warn drivers behind of a hazard ahead on a motorway or dual carriageway", "Park on double yellows", "Show you're lost"], 1, "Only briefly on motorways or unrestricted dual carriageways to warn of a hazard ahead."],
    ["What should you do before moving off from the side of the road?", ["Just indicate", "Check mirrors and your blind spot", "Sound the horn", "Flash your lights"], 1, "Always do full observations, including the blind spot, before pulling away."]
  ];
  function quiz() {
    var root = $("[data-tool='quiz']");
    if (!root) return;
    var qEl = $(".quiz__q", root), opts = $(".quiz__opts", root), exp = $(".quiz__explain", root);
    var meta = $(".js-meta", root), scoreEl = $(".js-score", root), next = $(".js-next", root), bar = $(".progress span", root);
    var stage = $(".js-stage", root), end = $(".js-end", root);
    var set = [], idx = 0, score = 0, ROUND = 10;
    function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
    function start() { set = shuffle(QUESTIONS.slice()).slice(0, ROUND); idx = 0; score = 0; stage.classList.remove("hide"); end.classList.add("hide"); show(); }
    function show() {
      var q = set[idx];
      meta.textContent = "Question " + (idx + 1) + " / " + ROUND;
      scoreEl.textContent = "Score " + score;
      bar.style.width = (idx / ROUND) * 100 + "%";
      qEl.textContent = q[0];
      exp.classList.remove("is-visible");
      next.classList.add("hide");
      opts.innerHTML = "";
      q[1].forEach(function (o, i) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "quiz__opt";
        b.innerHTML = "<b>" + "ABCD"[i] + "</b><span></span>";
        b.lastChild.textContent = o;
        b.addEventListener("click", function () { answer(i, b); });
        opts.appendChild(b);
      });
    }
    function answer(i, btn) {
      var q = set[idx];
      $$(".quiz__opt", opts).forEach(function (b, bi) { b.disabled = true; if (bi === q[2]) b.classList.add("is-right"); });
      if (i === q[2]) score++; else btn.classList.add("is-wrong");
      scoreEl.textContent = "Score " + score;
      exp.textContent = (i === q[2] ? "Correct! " : "Not quite. ") + q[3];
      exp.classList.add("is-visible");
      next.classList.remove("hide");
      next.textContent = idx === ROUND - 1 ? "See my result" : "Next question →";
      next.focus();
    }
    next.addEventListener("click", function () {
      idx++;
      if (idx < ROUND) return show();
      bar.style.width = "100%";
      stage.classList.add("hide");
      end.classList.remove("hide");
      $(".js-final", end).textContent = score + " / " + ROUND;
      $(".js-verdict", end).textContent = score >= 9 ? "Outstanding — you're thinking like a theory test pass." : score >= 7 ? "Solid! A little more revision and you'll smash it." : "Keep going — the DriveSQ Student Portal has a full mock theory test to help you practise.";
      if (score >= 8) SQ.confetti();
    });
    $$(".js-restart", root).forEach(function (b) { b.addEventListener("click", start); });
    start();
  }

  /* ------------------------------------------------------
     HAZARD GAME
     ------------------------------------------------------ */
  var SCENES = [
    { name: "School run", time: "08:35", hazards: [
      { type: "child", x: 300, y: 395, label: "Child stepping out between parked cars" },
      { type: "ball", x: 370, y: 455, label: "Ball rolling into the road" },
      { type: "car-out", x: 640, y: 360, label: "Car pulling out of a side road" }
    ], decor: ["parked-left", "school-sign"] },
    { name: "High street", time: "13:10", hazards: [
      { type: "cyclist", x: 560, y: 420, label: "Cyclist close to the kerb" },
      { type: "door", x: 250, y: 410, label: "Car door opening" },
      { type: "pedestrian", x: 470, y: 330, label: "Pedestrian at the zebra crossing" }
    ], decor: ["zebra", "parked-left", "shops"] },
    { name: "Bus stop", time: "17:45", hazards: [
      { type: "bus", x: 600, y: 370, label: "Bus pulling away from the stop" },
      { type: "runner", x: 690, y: 430, label: "Person running for the bus" },
      { type: "dog", x: 210, y: 470, label: "Dog off its lead near the road" }
    ], decor: ["shops"] }
  ];
  function drawScene(svg, scene) {
    var NS = "http://www.w3.org/2000/svg";
    var night = scene.time === "17:45";
    var s = "";
    s += "<defs><linearGradient id='sky' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='" + (night ? "#1a1030" : "#28344a") + "'/><stop offset='1' stop-color='" + (night ? "#40122a" : "#5d6c80") + "'/></linearGradient>" +
      "<linearGradient id='road' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#2b2d33'/><stop offset='1' stop-color='#17181c'/></linearGradient></defs>";
    s += "<rect width='800' height='500' fill='url(#sky)'/>";
    s += "<rect y='260' width='800' height='240' fill='#1d2a1f'/>";
    // buildings
    for (var i = 0; i < 9; i++) {
      var bx = i * 95 - 10, bh = 60 + ((i * 37) % 70);
      s += "<rect x='" + bx + "' y='" + (262 - bh) + "' width='86' height='" + bh + "' fill='" + (i % 2 ? "#2f3542" : "#3a3f4d") + "'/>";
      for (var wy = 262 - bh + 12; wy < 250; wy += 22) for (var wx = bx + 10; wx < bx + 76; wx += 22)
        s += "<rect x='" + wx + "' y='" + wy + "' width='10' height='12' fill='" + (night && (wx + wy) % 3 ? "#ffcf6b" : "#56607a") + "' opacity='.8'/>";
    }
    // road perspective
    s += "<polygon points='330,262 470,262 800,500 0,500' fill='url(#road)'/>";
    s += "<polygon points='310,262 330,262 0,500 0,470' fill='#8a8f99'/><polygon points='470,262 490,262 800,470 800,500' fill='#8a8f99'/>";
    for (var d = 0; d < 7; d++) {
      var t1 = d / 7, t2 = (d + 0.5) / 7;
      var y1 = 262 + t1 * t1 * 238, y2 = 262 + t2 * t2 * 238;
      var w1 = 1 + t1 * 6, w2 = 1 + t2 * 6;
      s += "<polygon points='" + (400 - w1) + "," + y1 + " " + (400 + w1) + "," + y1 + " " + (400 + w2) + "," + y2 + " " + (400 - w2) + "," + y2 + "' fill='#f2f2f2' opacity='.85'/>";
    }
    if (scene.decor.indexOf("zebra") > -1) for (var z = 0; z < 8; z++) s += "<rect x='" + (320 + z * 22) + "' y='318' width='12' height='16' fill='#eee' opacity='.9'/>";
    if (scene.decor.indexOf("parked-left") > -1) s += "<g><rect x='150' y='380' width='120' height='50' rx='12' fill='#7a1f1f'/><rect x='170' y='362' width='80' height='30' rx='8' fill='#5c1818'/><circle cx='175' cy='432' r='12' fill='#111'/><circle cx='245' cy='432' r='12' fill='#111'/></g>" +
      "<g><rect x='20' y='420' width='130' height='56' rx='12' fill='#2f4f7a'/><rect x='40' y='400' width='88' height='32' rx='8' fill='#243f63'/><circle cx='48' cy='478' r='13' fill='#111'/><circle cx='122' cy='478' r='13' fill='#111'/></g>";
    if (scene.decor.indexOf("school-sign") > -1) s += "<g><rect x='528' y='250' width='4' height='60' fill='#aaa'/><polygon points='530,212 556,256 504,256' fill='#fff' stroke='#d00' stroke-width='5'/><circle cx='524' cy='238' r='4' fill='#111'/><circle cx='536' cy='240' r='4' fill='#111'/></g>";
    if (scene.decor.indexOf("shops") > -1) s += "<rect x='560' y='230' width='240' height='32' fill='#ff1f1f' opacity='.25'/>";
    svg.innerHTML = s;
    scene.hazards.forEach(function (h, hi) {
      var g = document.createElementNS(NS, "g");
      g.setAttribute("class", "hazard-item");
      var x = h.x, y = h.y, art = "";
      switch (h.type) {
        case "child": art = "<circle cx='" + x + "' cy='" + (y - 38) + "' r='9' fill='#f1c7a1'/><rect x='" + (x - 9) + "' y='" + (y - 29) + "' width='18' height='26' rx='5' fill='#e6c200'/><rect x='" + (x - 8) + "' y='" + (y - 4) + "' width='6' height='18' fill='#223'/><rect x='" + (x + 2) + "' y='" + (y - 4) + "' width='6' height='18' fill='#223'/>"; break;
        case "ball": art = "<circle cx='" + x + "' cy='" + y + "' r='11' fill='#ff3b3b'/><path d='M" + (x - 11) + " " + y + "h22' stroke='#fff' stroke-width='3'/>"; break;
        case "car-out": art = "<rect x='" + (x - 50) + "' y='" + (y - 20) + "' width='100' height='40' rx='10' fill='#c9c9c9'/><rect x='" + (x - 30) + "' y='" + (y - 36) + "' width='60' height='22' rx='6' fill='#9aa'/><circle cx='" + (x - 30) + "' cy='" + (y + 20) + "' r='10' fill='#111'/><circle cx='" + (x + 30) + "' cy='" + (y + 20) + "' r='10' fill='#111'/><circle cx='" + (x - 46) + "' cy='" + y + "' r='5' fill='#ffb020'/>"; break;
        case "cyclist": art = "<circle cx='" + (x - 16) + "' cy='" + (y + 14) + "' r='14' fill='none' stroke='#ddd' stroke-width='3'/><circle cx='" + (x + 16) + "' cy='" + (y + 14) + "' r='14' fill='none' stroke='#ddd' stroke-width='3'/><path d='M" + (x - 16) + " " + (y + 14) + "L" + x + " " + (y - 6) + "L" + (x + 16) + " " + (y + 14) + "' stroke='#ddd' stroke-width='3' fill='none'/><circle cx='" + x + "' cy='" + (y - 34) + "' r='8' fill='#f1c7a1'/><rect x='" + (x - 6) + "' y='" + (y - 26) + "' width='12' height='22' rx='4' fill='#1fbf6a'/>"; break;
        case "door": art = "<polygon points='" + (x - 10) + "," + (y - 30) + " " + (x + 30) + "," + (y - 40) + " " + (x + 30) + "," + (y + 10) + " " + (x - 10) + "," + (y + 14) + "' fill='#a33' stroke='#fff' stroke-width='2'/>"; break;
        case "pedestrian": case "runner": art = "<circle cx='" + x + "' cy='" + (y - 40) + "' r='9' fill='#c58c5c'/><rect x='" + (x - 9) + "' y='" + (y - 31) + "' width='18' height='30' rx='5' fill='" + (h.type === "runner" ? "#3b82f6" : "#ddd") + "'/><rect x='" + (x - 8) + "' y='" + (y - 2) + "' width='6' height='22' fill='#333' transform='rotate(" + (h.type === "runner" ? -20 : 0) + " " + x + " " + y + ")'/><rect x='" + (x + 2) + "' y='" + (y - 2) + "' width='6' height='22' fill='#333' transform='rotate(" + (h.type === "runner" ? 20 : 0) + " " + x + " " + y + ")'/>"; break;
        case "bus": art = "<rect x='" + (x - 80) + "' y='" + (y - 60) + "' width='160' height='90' rx='10' fill='#d4161d'/><rect x='" + (x - 70) + "' y='" + (y - 50) + "' width='140' height='30' fill='#9fd3ff' opacity='.7'/><circle cx='" + (x - 50) + "' cy='" + (y + 32) + "' r='13' fill='#111'/><circle cx='" + (x + 50) + "' cy='" + (y + 32) + "' r='13' fill='#111'/><circle cx='" + (x - 78) + "' cy='" + (y + 10) + "' r='5' fill='#ffb020'/>"; break;
        case "dog": art = "<ellipse cx='" + x + "' cy='" + y + "' rx='22' ry='11' fill='#8b5a2b'/><circle cx='" + (x + 22) + "' cy='" + (y - 10) + "' r='9' fill='#8b5a2b'/><rect x='" + (x - 16) + "' y='" + (y + 6) + "' width='5' height='14' fill='#8b5a2b'/><rect x='" + (x + 10) + "' y='" + (y + 6) + "' width='5' height='14' fill='#8b5a2b'/>"; break;
      }
      g.innerHTML = art + "<circle class='hazard-hit' data-i='" + hi + "' cx='" + x + "' cy='" + (y - 12) + "' r='" + (h.type === "bus" || h.type === "car-out" ? 75 : 46) + "' fill='transparent'/>";
      svg.appendChild(g);
    });
  }
  function hazardGame() {
    var root = $("[data-tool='hazard']");
    if (!root) return;
    var stage = $(".hazard-stage", root), svg = $("svg", stage);
    var hudScene = $(".js-scene", root), hudFound = $(".js-found", root), hudTime = $(".js-time", root), hudScore = $(".js-hscore", root);
    var startBtn = $(".js-hstart", root), log = $(".js-log", root), end = $(".js-hend", root);
    var si = 0, found = [], score = 0, misses = 0, spotted = 0, timer = null, left = 0, playing = false;
    function mark(x, y, miss) {
      var r = svg.getBoundingClientRect();
      var m = document.createElement("span");
      m.className = "hazard-mark" + (miss ? " hazard-mark--miss" : "");
      m.style.left = ((x / 800) * r.width) + "px";
      m.style.top = ((y / 500) * r.height) + "px";
      stage.appendChild(m);
      if (miss) setTimeout(function () { m.remove(); }, 700);
    }
    function load() {
      found = [];
      $$(".hazard-mark", stage).forEach(function (m) { m.remove(); });
      var sc = SCENES[si];
      drawScene(svg, sc);
      hudScene.textContent = (si + 1) + "/" + SCENES.length + " · " + sc.name;
      hudFound.textContent = "0/" + sc.hazards.length;
      left = 20; hudTime.textContent = left + "s";
      clearInterval(timer);
      timer = setInterval(function () {
        left--; hudTime.textContent = left + "s";
        if (left <= 0) nextScene();
      }, 1000);
    }
    function nextScene() {
      clearInterval(timer);
      var sc = SCENES[si];
      sc.hazards.forEach(function (h, i) { if (found.indexOf(i) < 0) log.insertAdjacentHTML("beforeend", "<li>Missed: " + h.label + "</li>"); });
      si++;
      if (si < SCENES.length) setTimeout(load, 600);
      else finish();
    }
    function finish() {
      playing = false;
      var total = SCENES.reduce(function (s, x) { return s + x.hazards.length; }, 0);
      end.classList.remove("hide");
      $(".js-hfinal", end).textContent = score + " pts";
      $(".js-hsum", end).textContent = "You spotted " + spotted + " of " + total + " hazards with " + misses + " wrong click" + (misses === 1 ? "" : "s") + ".";
      if (spotted === total && misses <= 2) SQ.confetti();
    }
    svg.addEventListener("click", function (e) {
      if (!playing) return;
      var r = svg.getBoundingClientRect();
      var x = ((e.clientX - r.left) / r.width) * 800, y = ((e.clientY - r.top) / r.height) * 500;
      var hit = e.target.closest(".hazard-hit");
      if (hit) {
        var i = parseInt(hit.getAttribute("data-i"), 10);
        if (found.indexOf(i) > -1) return;
        found.push(i);
        spotted++;
        var pts = Math.max(1, Math.ceil(left / 4));
        score += pts;
        mark(x, y, false);
        log.insertAdjacentHTML("beforeend", "<li><b>+" + pts + "</b> " + SCENES[si].hazards[i].label + "</li>");
        hudFound.textContent = found.length + "/" + SCENES[si].hazards.length;
        if (found.length === SCENES[si].hazards.length) nextScene();
      } else {
        misses++;
        score = Math.max(0, score - 1);
        mark(x, y, true);
      }
      hudScore.textContent = score;
    });
    startBtn.addEventListener("click", function () {
      si = 0; score = 0; misses = 0; spotted = 0; playing = true; log.innerHTML = ""; end.classList.add("hide");
      hudScore.textContent = "0";
      startBtn.textContent = "Restart";
      load();
    });
    drawScene(svg, SCENES[0]);
  }


  /* ------------------------------------------------------
     SQ ASSISTANT — rule-based chat assistant (runs in the browser, no data stored)
     ------------------------------------------------------ */
  function chatbot() {
    if ($(".bot")) return;
    var root = (document.querySelector("link[rel='stylesheet'][href*='assets/css']") || {}).getAttribute ? document.querySelector("link[rel='stylesheet'][href*='assets/css']").getAttribute("href").replace("assets/css/sq.css", "") : "";
    var P = SQ.prices;
    var launch = document.createElement("button");
    launch.type = "button";
    launch.className = "bot-launch";
    launch.setAttribute("aria-label", "Open SQ Assistant chat");
    launch.innerHTML = "<span class='bot-launch__logo'>SQ</span><span class='bot-launch__dot'></span><b>Ask SQ Assistant</b>";
    var box = document.createElement("section");
    box.className = "bot";
    box.setAttribute("aria-label", "SQ Assistant");
    box.innerHTML = "<div class='bot__head'><span class='bot-launch__logo'>SQ</span><div><b>SQ Assistant</b><small>Automated assistant · instant answers</small></div><button class='bot__close' type='button' aria-label='Close chat'>✕</button></div>" +
      "<div class='bot__log' role='log' aria-live='polite'></div><div class='bot__chips'></div>" +
      "<form class='bot__form'><input type='text' aria-label='Type your question' placeholder='Ask about prices, postcodes, discounts…' autocomplete='off'><button type='submit' aria-label='Send'><svg viewBox='0 0 24 24' width='20' height='20' fill='none' stroke='currentColor' stroke-width='2.4'><path d='M5 12h14M13 6l6 6-6 6'/></svg></button></form>" +
      "<div class='bot__foot'>Automated answers. For bookings, a real person replies on WhatsApp.</div>";
    document.body.appendChild(launch);
    document.body.appendChild(box);
    var log = $(".bot__log", box), chips = $(".bot__chips", box), form = $(".bot__form", box), input = $("input", box);
    var started = false, awaitingPostcode = false;

    function add(html, who) {
      var m = document.createElement("div");
      m.className = "msg msg--" + who;
      if (who === "user") m.textContent = html; else m.innerHTML = html;
      log.appendChild(m);
      log.scrollTop = log.scrollHeight;
    }
    function botSay(html, nextChips) {
      var t = document.createElement("div");
      t.className = "msg msg--bot typing";
      t.innerHTML = "<i></i><i></i><i></i>";
      log.appendChild(t);
      log.scrollTop = log.scrollHeight;
      setTimeout(function () { t.remove(); add(html, "bot"); setChips(nextChips || DEFAULT_CHIPS); }, reduceMotion ? 50 : 650 + Math.min(900, html.length * 3));
    }
    function setChips(list) {
      chips.innerHTML = "";
      list.forEach(function (c) {
        var b = document.createElement("button");
        b.type = "button";
        b.textContent = c;
        b.addEventListener("click", function () { handle(c); });
        chips.appendChild(b);
      });
    }
    var DEFAULT_CHIPS = ["💷 Prices", "🏥 NHS discount", "🎓 Student discount", "📍 Check my postcode", "⚡ Intensive", "📱 Student Portal", "📅 Book a lesson"];
    var wa = function (msg, label) { return "<a href='" + SQ.waLink(msg) + "' target='_blank' rel='noopener'>" + (label || "Message us on WhatsApp") + "</a>"; };
    var link = function (href, label) { return "<a href='" + root + href + "'>" + label + "</a>"; };

    var INTENTS = [
      { k: ["hello", "hi", "hey", "salam", "salaam", "good morning", "good evening"], r: function () { return "Hi! 👋 I'm the SQ Assistant. I can help with prices, discounts, postcodes, lessons, intensive courses and the DriveSQ Student Portal. What would you like to know?"; } },
      { w: 3, k: ["nhs", "nurse", "doctor", "hospital", "healthcare"], r: function () { return "🏥 <b>NHS discount:</b> 10 hours for <b>£" + P.blockDiscount + "</b> instead of £" + P.block + " — you save £" + (P.block - P.blockDiscount) + ".<br>Proof: NHS ID badge, NHS email or payslip.<br>" + wa("Hi! I work for the NHS and I'd like the NHS discount (10 hours for £320).", "Claim it on WhatsApp"); } },
      { w: 3, k: ["student", "uni", "university", "college", "sixth form", "mmu", "salford uni"], r: function () { return "🎓 <b>Student discount:</b> 10 hours for <b>£" + P.blockDiscount + "</b> (normally £" + P.block + ").<br>Proof: valid student ID or enrolment letter.<br>" + wa("Hi! I'm a student and I'd like the student discount (10 hours for £320).", "Claim it on WhatsApp"); } },
      { w: 3, k: ["m16", "m18", "m19", "levenshulme", "gorton", "burnage", "old trafford", "whalley range", "firswood", "abbey hey", "special offer", "offer"], r: function () { return "🔥 <b>Special offer:</b> learners picked up in <b>M16, M18 or M19</b> get 10 hours for <b>£" + P.blockDiscount + "</b>. That covers Old Trafford, Whalley Range, Firswood, Gorton, Abbey Hey, Levenshulme and Burnage.<br>" + link("offer-m16-m18-m19.html", "See the offer") + " or type your postcode and I'll check it."; } },
      { k: ["discount", "cheap", "deal", "save", "offers", "promo"], r: function () { return "💸 Our discounts — all 10 hours for <b>£" + P.blockDiscount + "</b> (save £" + (P.block - P.blockDiscount) + "):<br>• NHS staff<br>• Students<br>• Learners in M16, M18 &amp; M19<br>More discounts are coming soon. " + link("discounts.html", "All discounts →"); }, chips: ["🏥 NHS discount", "🎓 Student discount", "📍 Check my postcode"] },
      { k: ["price", "cost", "how much", "fee", "rate", "£", "pound", "expensive", "per hour", "hourly"], r: function () { return "💷 <b>Our prices</b> (manual &amp; automatic):<table><tr><td>2-hour lesson</td><td>£" + P.twoHour + "</td></tr><tr><td>Hourly rate</td><td>£" + P.hourly + "</td></tr><tr><td>Single 1-hour session</td><td>£" + P.single + "</td></tr><tr><td>10-hour block</td><td>£" + P.block + "</td></tr><tr><td>10 hrs NHS / student / M16·M18·M19</td><td>£" + P.blockDiscount + "</td></tr></table>" + link("prices.html#builder", "Build your own package →"); }, chips: ["🏥 NHS discount", "🎓 Student discount", "🧮 How many hours?", "📅 Book a lesson"] },
      { k: ["block", "10 hour", "ten hour", "package", "bundle"], r: function () { return "📦 A <b>10-hour block</b> is £" + P.block + ", or <b>£" + P.blockDiscount + "</b> for NHS staff, students and M16/M18/M19 learners. Use the " + link("prices.html#builder", "package builder") + " to see any number of hours priced live."; } },
      { k: ["1 hour", "one hour", "single", "2 hour", "two hour", "minimum", "lesson length", "how long"], r: function () { return "⏱️ Our standard lesson is <b>2 hours for £" + P.twoHour + "</b> — two hours gives you time to really progress. If you just want one hour, a single session is <b>£" + P.single + "</b>."; } },
      { k: ["intensive", "fast", "quick", "crash", "asap", "urgent", "fast track", "fast-track"], r: function () { return "⚡ <b>Intensive courses:</b> 10–40 hours over 1–4 weeks, manual or automatic. Try the " + link("intensive.html", "intensive course planner") + " to see your schedule and cost."; } },
      { k: ["automatic", "auto"], r: function () { return "🚗 Yes, we teach <b>automatic</b> — same price as manual: £" + P.twoHour + " for 2 hours."; } },
      { k: ["manual", "clutch", "gears"], r: function () { return "⚙️ Yes, we teach <b>manual</b> — £" + P.twoHour + " for 2 hours, same as automatic."; } },
      { k: ["portal", "app", "drivesq student", "progress", "track"], r: function () { return "📱 Every SQ learner gets the <b>DriveSQ Student Portal</b> free: 23 skills tracked, a theory library, 50-question mock tests, instructor messaging and a test readiness checklist.<br>" + link("student-portal.html", "How it works") + " · <a href='" + SQ.portalStudent + "' target='_blank' rel='noopener'>Student login ↗</a>"; } },
      { w: 3, k: ["instructor portal", "instructor login", "i am an instructor", "adi", "pdi", "become an instructor", "join"], r: function () { return "👨‍🏫 Instructors use the <b>DriveSQ Instructor Portal</b> to manage pupils, bookings and progress. <a href='" + SQ.portalInstructor + "' target='_blank' rel='noopener'>Instructor login ↗</a><br>Want to teach with us? " + wa("Hi! I'm a driving instructor and I'm interested in working with SQ Driving School.", "Message us"); } },
      { k: ["area", "cover", "where", "location", "bolton", "bury", "oldham", "rochdale", "stockport", "tameside", "trafford", "salford", "wigan", "manchester", "near me"], r: function () { return "📍 We cover <b>all of Greater Manchester</b>: Manchester, Salford, Trafford, Stockport, Tameside, Oldham, Rochdale, Bury, Bolton and Wigan. Type your postcode and I'll check it for you!"; }, after: function () { awaitingPostcode = true; }, chips: ["📍 Check my postcode", "💷 Prices"] },
      { w: 3, k: ["check my postcode", "postcode", "post code"], r: function () { return "📍 Sure — type your postcode (e.g. <b>M19 2AB</b> or just <b>M19</b>)."; }, after: function () { awaitingPostcode = true; }, chips: ["M19", "M16", "SK4", "BL1"] },
      { k: ["theory", "hazard perception", "mock"], r: function () { return "📚 For your theory test: try our free " + link("theory-quiz.html", "Highway Code quiz") + " and " + link("hazard-game.html", "spot-the-hazard game") + ". SQ learners also get full 50-question mock tests in the DriveSQ Student Portal. Book the real test on <a href='https://www.gov.uk/book-theory-test' target='_blank' rel='noopener'>GOV.UK</a>."; } },
      { k: ["test", "book my test", "test centre", "test center", "practical", "exam"], r: function () { return "🏁 You book your practical test yourself on <a href='https://www.gov.uk/book-driving-test' target='_blank' rel='noopener'>GOV.UK</a>. Our " + link("test-centres.html", "test centre guide") + " covers every Greater Manchester centre. We can provide the car and a warm-up lesson on test day."; } },
      { k: ["how many hours", "how many lessons", "how many", "hours do i need"], r: function () { return "🧮 Most learners need roughly 40–45 hours of lessons — but it depends on you. Try our " + link("tools.html#lessons", "lesson calculator") + " for a personal estimate in 5 questions."; } },
      { k: ["nervous", "anxious", "scared", "anxiety", "afraid"], r: function () { return "💙 You're in good hands. We go at your pace, start on quiet roads, and your portal shows your progress so you can see how far you've come. Many people feel exactly the same at the start."; } },
      { k: ["fail", "failed"], r: function () { return "That's frustrating — but very common. Bring your test report and we'll focus your lessons on those faults. Try a 10-hour block to get test-sharp again."; } },
      { k: ["motorway"], r: function () { return "🛣️ Yes — learners can have motorway lessons with an approved instructor in a dual-controlled car. Ask us to add one to your package."; } },
      { k: ["pay", "payment", "card", "cash", "bank"], r: function () { return "💳 " + wa("Hi! How can I pay for lessons?", "Message us") + " and we'll explain payment options. Block bookings are paid in advance."; } },
      { k: ["owner", "own", "who owns", "drivesq", "who are you", "about"], r: function () { return "SQ Driving School is a brand <b>owned and managed by DriveSQ</b>. Crafted by Mohammed Qaim Abbas. " + link("about.html", "About us →"); } },
      { k: ["book", "start", "sign up", "enrol", "enroll", "available", "availability", "slot"], r: function () { return "📅 Let's get you booked! The fastest way is WhatsApp — a real person replies.<br>" + wa("Hi SQ Driving School! I'd like to book driving lessons.", "Book on WhatsApp") + " · or call <a href='tel:" + SQ.phoneIntl + "'>" + SQ.phone + "</a>"; } },
      { k: ["contact", "phone", "call", "number", "whatsapp", "email", "human", "person", "speak"], r: function () { return "📞 WhatsApp or call <a href='tel:" + SQ.phoneIntl + "'>" + SQ.phone + "</a>.<br>" + wa("Hi SQ Driving School!", "Open WhatsApp"); } },
      { k: ["thank", "thanks", "cheers", "ta"], r: function () { return "You're welcome! 🚗 Anything else?"; } }
    ];

    function postcodeReply(text) {
      var r = SQ.checkPostcode(text);
      if (r.status === "covered" && r.offer) return "🎉 <b>" + r.outward + "</b> (" + r.area + ") — we cover you <b>and</b> you unlock the special offer: 10 hours for <b>£" + P.blockDiscount + "</b>!<br>" + wa("Hi! My postcode is " + r.outward + " — I'd like the 10 hours for £320 offer.", "Claim on WhatsApp");
      if (r.status === "covered") return "✅ Yes! We cover <b>" + r.outward + "</b> — " + r.area + ", " + r.borough + ". Lessons are £" + P.twoHour + " for 2 hours.<br>" + wa("Hi! My postcode is " + r.outward + " and I'd like to book lessons.", "Book on WhatsApp");
      if (r.status === "partial") return "🤔 <b>" + r.outward + "</b> (" + r.area + ") is on the edge of our area. " + wa("Hi! Do you cover " + r.outward + "?", "Ask us on WhatsApp") + " and we'll confirm.";
      if (r.status === "outside") return "😕 <b>" + r.outward + "</b> looks outside Greater Manchester. If you can get to a Manchester pick-up point, " + wa("Hi! I'm in " + r.outward + " — could you pick me up somewhere in Manchester?", "message us") + ".";
      return null;
    }

    function handle(raw) {
      var text = String(raw).trim();
      if (!text) return;
      add(text, "user");
      input.value = "";
      var clean = text.replace(/[^\w£\s'-]/g, " ").toLowerCase().trim();
      var looksPostcode = /^[a-z]{1,2}\d[a-z\d]?(\s*\d[a-z]{2})?$/i.test(clean.replace(/\s+/g, " "));
      if (awaitingPostcode || looksPostcode) {
        var pr = postcodeReply(clean);
        if (pr) { awaitingPostcode = false; return botSay(pr); }
      }
      var best = null, bestScore = 0;
      INTENTS.forEach(function (it) {
        var sc = 0;
        it.k.forEach(function (k) { if ((" " + clean + " ").indexOf(k.length <= 3 ? " " + k + " " : k) > -1) sc += k.length * (it.w || 1); });
        if (sc > bestScore) { bestScore = sc; best = it; }
      });
      if (best) {
        awaitingPostcode = false;
        if (best.after) best.after();
        return botSay(best.r(), best.chips);
      }
      botSay("I'm not sure about that one — but a real person can help! " + wa("Hi SQ Driving School! I have a question: " + text, "Ask on WhatsApp") + "<br>Or try one of these:");
    }

    function open() {
      box.classList.add("is-open");
      launch.setAttribute("aria-expanded", "true");
      if (!started) {
        started = true;
        botSay("Hi! 👋 I'm the <b>SQ Assistant</b>. Ask me anything about lessons, prices, discounts or postcodes — or tap an option below.");
      }
      setTimeout(function () { input.focus(); }, 300);
    }
    function close() { box.classList.remove("is-open"); launch.setAttribute("aria-expanded", "false"); launch.focus(); }
    launch.addEventListener("click", function () { box.classList.contains("is-open") ? close() : open(); });
    $(".bot__close", box).addEventListener("click", close);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && box.classList.contains("is-open")) close(); });
    form.addEventListener("submit", function (e) { e.preventDefault(); handle(input.value); });
    $$("[data-open-bot]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); open(); }); });
    SQ.openBot = open;
  }

  /* ------------------------------------------------------
     ROAD SIGN FLASHCARDS
     ------------------------------------------------------ */
  function flashcards() {
    var root = $("[data-tool='flash']");
    if (!root) return;
    var known = 0, seen = {};
    var score = $(".js-known", root);
    $$(".flash", root).forEach(function (card, i) {
      card.addEventListener("click", function (e) {
        if (e.target.closest("button")) return;
        card.classList.toggle("is-flipped");
      });
      card.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); card.classList.toggle("is-flipped"); } });
      $$("[data-know]", card).forEach(function (b) {
        b.addEventListener("click", function () {
          var k = b.getAttribute("data-know") === "yes";
          if (seen[i] === undefined) { seen[i] = k; if (k) known++; }
          else if (seen[i] !== k) { known += k ? 1 : -1; seen[i] = k; }
          score.textContent = known;
          card.style.borderRadius = "22px";
          card.style.boxShadow = k ? "0 0 0 2px #22e07a" : "0 0 0 2px #ff1f1f";
          if (known === $$(".flash", root).length) SQ.confetti();
        });
      });
    });
    var shuffle = $(".js-shuffle", root);
    if (shuffle) shuffle.addEventListener("click", function () {
      var grid = $(".js-flash-grid", root);
      var cards = $$(".flash", grid);
      cards.sort(function () { return Math.random() - 0.5; }).forEach(function (c) { c.classList.remove("is-flipped"); grid.appendChild(c); });
    });
  }

  /* ------------------------------------------------------
     DASHBOARD WARNING LIGHTS
     ------------------------------------------------------ */
  function dashLights() {
    var root = $("[data-tool='dash']");
    if (!root) return;
    var info = $(".dinfo", root);
    var lights = $$(".dlight", root);
    function show(l) {
      lights.forEach(function (x) { x.classList.remove("is-on"); x.setAttribute("aria-pressed", "false"); });
      l.classList.add("is-on");
      l.setAttribute("aria-pressed", "true");
      info.innerHTML = "<span class='tag' style='color:var(--c);border-color:var(--c)'>" + l.getAttribute("data-level") + "</span><h3 class='mt-1'>" + l.getAttribute("data-name") + "</h3><p class='mb-0'>" + l.getAttribute("data-what") + "</p>";
      info.style.setProperty("--c", getComputedStyle(l).getPropertyValue("--c"));
    }
    lights.forEach(function (l) { l.addEventListener("click", function () { show(l); }); });
    var startBtn = $(".js-ignite", root);
    if (startBtn) startBtn.addEventListener("click", function () {
      lights.forEach(function (l, i) {
        setTimeout(function () { l.classList.add("is-on"); }, i * 60);
        setTimeout(function () { l.classList.remove("is-on"); }, 900 + i * 40);
      });
    });
  }

  /* ------------------------------------------------------
     YEAR + INIT
     ------------------------------------------------------ */
  function init() {
    $$(".js-year").forEach(function (el) { el.textContent = new Date().getFullYear(); });
    $$("[data-wa]").forEach(function (a) { a.href = SQ.waLink(a.getAttribute("data-wa")); a.target = "_blank"; a.rel = "noopener"; });
    preloader();
    nav();
    splitChars();
    reveal();
    scrollFx();
    interactions();
    transitions();
    canvasFx();
    speedLines();
    typewriter();
    toolPostcode();
    toolArea();
    toolBuilder();
    toolLessons();
    toolReadiness();
    toolCountdown();
    toolBudget();
    toolIntensive();
    contactForm();
    quiz();
    hazardGame();
    flashcards();
    dashLights();
    chatbot();
    var lang = store.get("sq-lang");
    if (lang && lang !== "en") applyLang(lang);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
