document.addEventListener("DOMContentLoaded", () => {
  const editButtons = document.querySelectorAll(".edit");
  const textInputs = document.querySelectorAll(".text");
  const saveButtons = document.querySelectorAll(".done");

  editButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const index = button.dataset.index;
      const inputField = textInputs[index];
      const saveButton = saveButtons[index];
      inputField.removeAttribute("readonly");
      inputField.focus();
      saveButton.style.display = "inline";
    });
  });

  saveButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const index = button.dataset.index;
      const inputField = textInputs[index];
      const task = inputField.value;
      inputField.setAttribute("readonly", true);
      button.style.display = "none";
      // Send updated task to the server for processing or update it locally
      console.log("Updated task:", task);
    });
  });
});
