<h1 style="color: #39ff14; text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 15px #39ff14, 0 0 20px #39ff14, 0 0 25px #39ff14, 0 0 30px #39ff14, 0 0 35px #39ff14;">👋 Hi, I'm @LukiDev17</h1>

<h2 style="color: #39ff14; text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14;">👀 Passionate about Private Servers</h2>

<h3 style="color: #39ff14; text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14;">🌱 Currently learning Python and Java</h3>

<h4 style="color: #39ff14; text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14;">💞️ Open to collaboration on private server projects</h4>

<p style="color: #39ff14; text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14;">📫 Reach me on Telegram: @LukiDev or <a href="https://web.telegram.org/k/#@LukiDev" style="color: #39ff14;">https://web.telegram.org/k/#@LukiDev</a></p>

<!-- First GIF -->
<img src="https://media.giphy.com/media/xTiTnqUxyWbsAXq7Ju/giphy.gif" alt="Private Server GIF" style="display: block; margin-left: auto; margin-right: auto; width: 50%;"/>

---

### 👨‍💻 My Tech Stack

- **Languages:** Python, C#, JavaScript, Java
- **Frameworks & Tools:** Node.js, Django, Flask, Express, MongoDB, SQLite
- **Other Skills:** Web Development, API Development, Database Management, Game Server Setup

---

### 📊 GitHub Stats

![Deine GitHub-Statistiken](https://github-readme-stats.vercel.app/api?username=LukiDev17&show_icons=true)

![Meistbenutzte Sprachen](https://github-readme-stats.vercel.app/api/top-langs/?username=LukiDev17&layout=compact&langs_count=10)

---

### 🚀 Latest Projects

<!-- Dynamically load your latest repositories -->
<div id="latest-projects">
  <!-- Placeholder for dynamically added projects -->
  <p>Loading your latest projects...</p>
</div>

<script>
  // Fetch latest repositories from GitHub
  fetch('https://api.github.com/users/LukiDev17/repos?sort=updated')
    .then(response => response.json())
    .then(repositories => {
      const projectsContainer = document.getElementById('latest-projects');
      projectsContainer.innerHTML = '';  // Clear loading text

      repositories.slice(0, 3).forEach(repo => {
        const projectElement = document.createElement('a');
        projectElement.href = repo.html_url;
        projectElement.innerHTML = `<p style="color: #39ff14;">${repo.name} - ${repo.description}</p>`;
        projectsContainer.appendChild(projectElement);
      });
    })
    .catch(error => {
      const projectsContainer = document.getElementById('latest-projects');
      projectsContainer.innerHTML = '<p>Error loading projects.</p>';
      console.error('Error fetching GitHub repos:', error);
    });
</script>

---

### 🌟 Contributions

- **Contributed to:** Several open-source private server projects and game development repositories.
- **Upcoming Work:** I'm working on creating tutorials and guides for setting up private game servers.

---

### 📱 Contact Me

Feel free to get in touch for collaboration or any project discussions:
- **Telegram:** [@LukiDev](https://web.telegram.org/k/#@LukiDev)

---

<footer style="text-align: center; margin-top: 20px;">
  <p style="color: #39ff14;">Made with ❤️ by @LukiDev17</p>
  <p><a href="https://github.com/LukiDev17" style="color: #39ff14;">GitHub Profile</a></p>
</footer>
