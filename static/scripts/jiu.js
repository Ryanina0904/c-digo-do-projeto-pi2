function toggleNotificationPopup() {
    var notificationPopup = document.getElementById('notificationPopup');
    var hasNotifications = true;
  
    if (hasNotifications) {
      // Lógica para preencher dinamicamente o conteúdo com notificações
      notificationPopup.innerHTML = '';  // Limpa o conteúdo existente
  
      // Suponha que você tenha uma lista de notificações
      var notifications = ['Notificação 1', 'Notificação 2', 'Notificação 3'];
  
      // Cria elementos <p> para cada notificação e os adiciona à telinha pequena
      notifications.forEach(function (notification) {
        var pElement = document.createElement('p');
        pElement.textContent = notification;
        notificationPopup.appendChild(pElement);
      });
  
      // Adiciona um botão de fechar
      var closeButton = document.createElement('button');
      closeButton.textContent = 'Fechar';
      closeButton.addEventListener('click', function () {
        notificationPopup.style.display = 'none';  // Oculta a tela de notificação ao clicar em Fechar
      });
      notificationPopup.appendChild(closeButton);
  
      // Exibe a telinha pequena
      notificationPopup.style.display = 'block';
    } else {
      alert('Não há notificações recentes.');
    }
  }
  
  document.addEventListener('DOMContentLoaded', function () {
    var notificationIcon = document.querySelector('.notification-icon');
    if (notificationIcon) {
      notificationIcon.addEventListener('click', toggleNotificationPopup);
    }
  });
  
  // Seu arquivo JavaScript/jQuery existente

// Função para exibir o modal de boas-vindas
function exibirModalBemVindo() {
    var modal = document.getElementById('modalBemVindo');
    modal.style.display = 'block';
  }
  
  // Função para fechar o modal de boas-vindas
  function fecharModalBemVindo() {
    var modal = document.getElementById('modalBemVindo');
    modal.style.display = 'none';
  }
  
  // Exiba o modal automaticamente quando a página for carregada (se houver um novo cadastro)
  document.addEventListener('DOMContentLoaded', function () {
    var cadastroRecente = localStorage.getItem('cadastroRecente');
    if (cadastroRecente) {
      exibirModalBemVindo();
      localStorage.removeItem('cadastroRecente');
    }
  });
  
