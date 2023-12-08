function validateCadastro() {
    var nome = document.getElementById('nome').value;
    var email = document.getElementById('cadastro_email').value;
    var senha = document.getElementById('senha').value;

    // Verificação básica (pode ser estendida conforme necessário)
    if (nome === '' || email === '' || senha === '') {
        alert('Por favor, preencha todos os campos.');
        return false;
    }

    // Verificar se o email é válido
    if (!validarEmail(email)) {
        alert('Por favor, insira um email válido.');
        return false;
    }

    // Enviar dados para o servidor
    var requestData = { nome: nome, email: email, senha: password };

    fetch('/api/cadastrar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Erro no cadastro');
        }
    })
    .then(data => {
        document.getElementById('mensagem').innerText = data.mensagem;
    })
    .catch(error => {
        document.getElementById('mensagem').innerText = 'Erro ao cadastrar: ' + error.message;
    });

    // Impede o envio do formulário (o que permitiria a recarga da página)
    return false;
}
function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}