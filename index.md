<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Happy - Artesanías</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #fffaf0;
      margin: 0;
      padding: 0;
    }
    .login-container, .content {
      display: none;
      text-align: center;
      padding: 50px;
    }
    .login-container.active, .content.active {
      display: block;
    }
    input[type="password"] {
      padding: 10px;
      font-size: 16px;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      background-color: #ff8c00;
      border: none;
      color: white;
      cursor: pointer;
      border-radius: 5px;
      margin-top: 10px;
    }
    h1 {
      color: #ff6600;
    }
    .products {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 20px;
      margin-top: 30px;
    }
    .product {
      border: 1px solid #ccc;
      border-radius: 10px;
      padding: 20px;
      width: 250px;
      background: #fff;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .product img {
      max-width: 100%;
      height: auto;
      border-radius: 5px;
    }
    .product h3 {
      margin: 10px 0 5px;
      color: #333;
    }
    .product p {
      margin: 0;
    }
    .buy-methods {
      margin-top: 30px;
    }
    .buy-methods ul {
      list-style-type: square;
      text-align: left;
      display: inline-block;
    }
  </style>
</head>
<body>

  <!-- LOGIN -->
  <div class="login-container active" id="login">
    <h1>Bienvenido a Happy</h1>
    <p>Por favor, ingresa la contraseña para acceder</p>
    <input type="password" id="password" placeholder="Contraseña" />
    <br />
    <button onclick="checkPassword()">Entrar</button>
    <p id="error" style="color:red;"></p>
  </div>

  <!-- CONTENIDO -->
  <div class="content" id="mainContent">
    <h1>Happy - Artesanías únicas</h1>
    
    <div class="products">
      <div class="product">
        <img src="https://via.placeholder.com/250x150?text=Collar+Artesanal" alt="Collar Artesanal">
        <h3>Collar artesanal</h3>
        <p>Precio: S/ 25.00</p>
      </div>
      <div class="product">
        <img src="https://via.placeholder.com/250x150?text=Bolso+Hecho+a+Mano" alt="Bolso artesanal">
        <h3>Bolso hecho a mano</h3>
        <p>Precio: S/ 45.00</p>
      </div>
      <div class="product">
        <img src="https://via.placeholder.com/250x150?text=Pulsera+Colorida" alt="Pulsera artesanal">
        <h3>Pulsera colorida</h3>
        <p>Precio: S/ 15.00</p>
      </div>
    </div>

    <div class="buy-methods">
      <h2>Modos de compra:</h2>
      <ul>
        <li>Pago contra entrega</li>
        <li>Yape o Plin</li>
        <li>Depósito bancario</li>
        <li>Pedidos por WhatsApp</li>
      </ul>
    </div>
  </div>

  <script>
    function checkPassword() {
      const password = document.getElementById("password").value;
      const correctPassword = "happy123"; // CAMBIA AQUÍ LA CONTRASEÑA

      if (password === correctPassword) {
        document.getElementById("login").classList.remove("active");
        document.getElementById("mainContent").classList.add("active");
      } else {
        document.getElementById("error").textContent = "Contraseña incorrecta. Intenta de nuevo.";
      }
    }
  </script>

</body>
</html>
