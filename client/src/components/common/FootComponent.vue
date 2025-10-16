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
  padding: 40px 0;       /* adjust padding instead of fixed height */
  text-align: center;
  font-family: Arial, sans-serif;
  /* remove fixed height and margin-top which cause layout issues */
  height: auto;
  margin-top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* container and icons */
.container { max-width: 1200px; margin:0 auto; display:flex; flex-direction:column; gap:12px; align-items:center; }
.footer-text { font-size: 20px; text-transform: uppercase; margin:0; }
.social-icons { display:flex; justify-content:center; align-items:center; gap:20px; }
.icon-link i { font-size: 2rem; } /* scale down a bit */
.icon-link { color:white; font-size: 20px; transition: color .3s; }
.icon-link:hover { color:#1abc9c; }

/* small screens */
@media (max-width: 480px) {
  .signup-box { padding: 1.5rem; width: 100%; }
  .footer-text { font-size: 18px; }
}
  </style>