const htmlElement = document.querySelector('html');

const changeMode = () => {
  htmlElement.classList.toggle('light');
  if (htmlElement.classList.contains('light')) {
    localStorage.setItem('mode', 'light');
  } else {
    localStorage.setItem('mode', 'dark');
  }
}

// Aplicar preferência ao carregar a página
const savedMode = localStorage.getItem('mode');
if (savedMode) {
  htmlElement.classList.add(savedMode);
}
