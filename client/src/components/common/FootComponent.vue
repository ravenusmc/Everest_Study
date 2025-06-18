<template>
    <footer class="footer">
      <div class="container">
        <p class="footer-text">Copyright &copy; 2025 Double Sun Productions</p>
        <div class="social-icons">
          <a
            href="https://www.linkedin.com/in/mcuddy1/"
            target="_blank"
            rel="noopener noreferrer"
            class="icon-link"
          >
            <i class="fab fa-linkedin"></i>
          </a>
          <a
            href="https://github.com/ravenusmc"
            target="_blank"
            rel="noopener noreferrer"
            class="icon-link"
          >
            <i class="fab fa-github"></i>
          </a>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: "FootComponent",
  };
  </script>
  
  <style scoped>
  .footer {
    background-color: #121212;
    color: white;
    padding: 20px 0;
    text-align: center;
    font-family: Arial, sans-serif;
    height: 300px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 50px;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
  }
  
  .footer-text {
    font-size: 36px;
    text-transform: uppercase;
    margin-bottom: 10px;
  }
  
  .social-icons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }

  .icon-link i {
  font-size: 4rem; /* Adjust this value as needed */
  }

  .icon-link {
    color: white;
    font-size: 24px;
    transition: color 0.3s ease;
  }
  
  .icon-link:hover {
    color: #1abc9c;
  }
  </style>