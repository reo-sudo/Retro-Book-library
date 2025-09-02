const form = document.getElementById('form');
        const username = document.getElementById('usernameID')
        const typingSound = new Audio('type.mp3');

        form.addEventListener('submit', function(e) {
            e.preventDefault();
        
        const usernameValue = username.value;

           localStorage.setItem('user-name', usernameValue);
            window.location.href = "home.html";
        })

        form.addEventListener('input', function(){
            typingSound.currentTime = 0;
            typingSound.play();

       
        });
        
    