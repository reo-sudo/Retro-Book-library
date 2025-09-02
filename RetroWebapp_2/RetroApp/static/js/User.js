const User_info = document.getElementById('User_info');
        const userText = document.getElementById('UserText');
        const username = localStorage.getItem('user-name');
        const typingSound = new Audio('type.mp3');

        document.getElementById('user-pro').textContent = username
        

        User_info.addEventListener('keydown', function(event){
            typingSound.currentTime = 0;
            typingSound.play();
            if (event.key === 'Enter') {

                const query = User_info.value;
                if (query === '/help') {
                    userText.textContent = `user commands:
                    /help: show all commands
                    /ChangeName: Changes name of user
                    /Return_Home: Returns User To Home Page`
                }  else if (query === '/ChangeName') {
                    const newName = prompt('Enter your new name: ')
                    if (newName && newName.trim() !== '') {
                        localStorage.setItem('user-name', newName)
                        userText.textContent = `Name Changed to ${newName}`;
                        document.getElementById('user-pro').textContent = newName;
                    } else {
                        userText.textContent = `Name not Changed.`;
                    }
                } else if (query === '/Return_Home') {
                    const CR = confirm('are you sure you wanna go to the home page')
                    if (CR) {
                        window.location.href = "home.html";
                        
                    }
                    
                } else {
                    userText.textContent = `unknown command: ${query}`;
                    userText.style.color = 'red';
                }

                user_info.value = '';

                }
            });
                
                        
