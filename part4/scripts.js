// Login function
async function login(event) {
    event.preventDefault();
    console.log('Login function called!');
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    console.log('Email:', email);
    console.log('Password:', password);
    
    try {
        console.log('Sending request to:', `${API_BASE_URL}/auth/login`);
        
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });
        
        console.log('Response status:', response.status);
        
        if (response.ok) {
            const data = await response.json();
            console.log('Login successful!', data);
            localStorage.setItem('token', data.access_token);
            window.location.href = 'places.html';
        } else {
            const error = await response.json();
            console.error('Login failed:', error);
            alert(error.error || 'Login failed');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during login');
    }
}