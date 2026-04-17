(() => {
  const chatForm = document.getElementById("chatForm");
  const userInput = document.getElementById("userInput");
  const chatBox = document.getElementById("chatBox");

  if (!chatForm || !userInput || !chatBox) {
    return;
  }

  function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.className = `msg ${sender}`;
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const question = userInput.value.trim();
    if (!question) {
      return;
    }

    addMessage(question, "user");
    userInput.value = "";

    const apiUrl = chatForm.dataset.apiUrl || "/api/assistant";

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await response.json();
      if (!response.ok) {
        addMessage(data.error || "تعذر الحصول على إجابة الآن.", "bot");
        return;
      }

      addMessage(data.answer, "bot");
    } catch (error) {
      addMessage("حدث خطأ في الاتصال بالخادم. حاول مرة أخرى.", "bot");
    }
  });
})();
