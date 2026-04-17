const posts = [
  {
    title: "ما هي المادة المظلمة؟",
    excerpt:
      "رغم أننا لا نراها مباشرة، إلا أن آثارها الجاذبية واضحة في دوران المجرات وحركتها.",
  },
  {
    title: "لماذا تبدو صور السُّدم ملوّنة جدًا؟",
    excerpt:
      "الألوان غالبًا تمثيل لأطوال موجية مختلفة التقطتها التلسكوبات، وليست دائمًا كما تراها العين البشرية.",
  },
  {
    title: "هل يمكن العيش على المريخ؟",
    excerpt:
      "التحديات تشمل الإشعاع، نقص الأوكسجين، ودرجات الحرارة القاسية، لكن الأبحاث تتقدم بسرعة.",
  },
  {
    title: "الثقوب السوداء فائقة الكتلة",
    excerpt:
      "تقع عادةً في مراكز المجرات وتؤثر بشكل كبير على بنية المجرة وتطورها عبر الزمن.",
  },
];

const grid = document.getElementById("postGrid");
const chatBox = document.getElementById("chatBox");
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");

posts.forEach((post) => {
  const card = document.createElement("article");
  card.className = "post";
  card.innerHTML = `<h4>${post.title}</h4><p>${post.excerpt}</p>`;
  grid.appendChild(card);
});

function addMessage(text, sender = "bot") {
  const msg = document.createElement("div");
  msg.className = `msg ${sender}`;
  msg.textContent = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function generateReply(question) {
  const q = question.toLowerCase();

  if (q.includes("مجرة") || q.includes("galaxy")) {
    return "المجرة هي نظام ضخم يحتوي نجومًا، غبارًا، غازًا، ومادة مظلمة مرتبطة بالجاذبية. درب التبانة مثال ممتاز.";
  }
  if (q.includes("سديم") || q.includes("nebula")) {
    return "السديم سحابة من الغاز والغبار في الفضاء، وقد يكون مكانًا لولادة النجوم أو بقايا انفجار نجم.";
  }
  if (q.includes("ثقب") || q.includes("black hole")) {
    return "الثقب الأسود منطقة جاذبيتها قوية جدًا لدرجة أن الضوء لا يهرب منها. يمكننا رصده عبر تأثيره على ما حوله.";
  }
  if (q.includes("شهب") || q.includes("meteor")) {
    return "لرصد الشهب بوضوح: ابتعد عن أضواء المدن، واختر ليلة صافية بعد منتصف الليل، وامنح عينيك 20 دقيقة للتأقلم.";
  }

  return "سؤال رائع ✨ يمكنني تبسيط أي موضوع فضائي لك، أو اقتراح مقال مناسب من المدونة حسب اهتمامك.";
}

chatForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = userInput.value.trim();
  if (!text) return;

  addMessage(text, "user");
  userInput.value = "";

  setTimeout(() => {
    addMessage(generateReply(text), "bot");
  }, 350);
});
