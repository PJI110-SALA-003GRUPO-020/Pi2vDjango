function aumentaZoom() {
    var elementosTexto = document.querySelectorAll('body *'); // Seleciona todos os elementos de texto na página
    for (let c = 0; c < elementosTexto.length; c++) {
      const elemento = elementosTexto[c];
      const fontSize = parseInt(window.getComputedStyle(elemento)['font-size']);
      elemento.style.fontSize = (fontSize + 1) + 'px';
    }
  }

  function diminuiZoom() {
    var elementosTexto = document.querySelectorAll('body *'); // Mesma seleção de elementos
    for (let c = 0; c < elementosTexto.length; c++) {
      const elemento = elementosTexto[c];
      const fontSize = parseInt(window.getComputedStyle(elemento)['font-size']);
      elemento.style.fontSize = (fontSize - 1) + 'px';
    }
  }

  function resetZoom() {
    var elementosTexto = document.querySelectorAll('body *'); // Mesma seleção de elementos
    for (let c = 0; c < elementosTexto.length; c++) {
      const elemento = elementosTexto[c];
      elemento.style.fontSize = ''; // Volta ao tamanho padrão
    }
  }

  function modoNoturno() {
    const elemento = document.querySelector("body");
    const bodyCS = window.getComputedStyle(elemento);
    const botoes = document.querySelectorAll("button");
    const links = document.querySelectorAll("a");
    const uls = document.querySelectorAll("ul");
    const lis = document.querySelectorAll("li");

    if (bodyCS.backgroundColor === "rgb(33, 37, 41)") {
        elemento.style.backgroundColor = "white";
        elemento.style.color = "#212529";
        
        for (const botao of botoes) {
            botao.style.color = "#212529";
        }

        for (const link of links) {
            link.style.color = "#212529";
        }

        for (const ul of uls) {
            ul.style.backgroundColor = "white";
        }

        for (const li of lis) {
            li.style.backgroundColor = "white";
        }
    } else {
        elemento.style.backgroundColor = "#212529";
        elemento.style.color = "white";
        
        for (const botao of botoes) {
            botao.style.color = "white";
        }

        for (const link of links) {
            link.style.color = "white";
        }

        for (const ul of uls) {
            ul.style.backgroundColor = "#212529";
        }

        for (const li of lis) {
            li.style.backgroundColor = "#212529";
        }
    }
}



  window.onload = function () {
    var botoes = document.querySelectorAll("i");
    for (let i = 0; i < botoes.length; i++) {
      botoes[0].addEventListener("click", aumentaZoom);
      botoes[1].addEventListener("click", diminuiZoom);
      botoes[2].addEventListener("click", resetZoom);
      botoes[3].addEventListener("click", modoNoturno);
    }
  }

