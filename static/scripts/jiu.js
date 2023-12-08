function toggleMenu() {
    const navMenu = document.querySelector('nav ul');
    navMenu.classList.toggle('show');
}
function adicionarComentario() {
    var nome = document.getElementById('nome').value;
    var comentario = document.getElementById('comentario').value;

    if (nome && comentario) {
        var novoComentario = document.createElement('div');
        novoComentario.innerHTML = '<strong>' + nome + ':</strong> ' + comentario;
        
        document.getElementById('comentarios').appendChild(novoComentario);

        // Limpar o formulário após adicionar o comentário
        document.getElementById('commentForm').reset();
    }
}