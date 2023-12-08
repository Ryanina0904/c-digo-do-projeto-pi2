function realizarLogin() {
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;

    var formData = new URLSearchParams();
    formData.append('email', email);
    formData.append('senha', senha);

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString(),  // Converte para a representação de string
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro HTTP - ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('mensagem').innerHTML = data.message;
        if (data.success) {
            console.log('Redirecionando para /home');
            window.location.href = '/home';
        }
    })
    .catch(error => {
        console.error('Erro durante a solicitação:', error);
        document.getElementById('mensagem').innerHTML = 'Erro durante a solicitação. Por favor, tente novamente.';
    });

    return false;  // Evitar que o formulário seja submetido
}
