<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Happy - Artesanías</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #fffef7;
      margin: 0;
      padding: 20px;
    }
    h1, h2 {
      color: #d35400;
      text-align: center;
    }
    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
      margin-top: 30px;
    }
    .product {
      border: 1px solid #ccc;
      padding: 10px;
      border-radius: 10px;
      background: white;
      text-align: center;
    }
    .product img {
      max-width: 100%;
      height: 120px;
      object-fit: cover;
      border-radius: 5px;
    }
    .product button {
      background-color: #e67e22;
      color: white;
      border: none;
      padding: 8px 12px;
      border-radius: 5px;
      cursor: pointer;
      margin-top: 10px;
    }
    #cart {
      margin-top: 40px;
      padding: 20px;
      background: #fef5e7;
      border-radius: 10px;
    }
    #cart ul {
      list-style: none;
      padding: 0;
    }
    #cart li {
      padding: 5px 0;
    }
    select, button#buyBtn {
      padding: 10px;
      margin-top: 10px;
      font-size: 16px;
    }
    #success {
      color: green;
      font-weight: bold;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>

  <h1>Happy - Artesanías Peruanas</h1>
  <div class="product-grid" id="productGrid">
    <!-- Aquí se cargan los productos automáticamente -->
  </div>

  <div id="cart">
    <h2>Carrito de compras</h2>
    <ul id="cartItems"></ul>
    <p><strong>Total: S/ <span id="total">0.00</span></strong></p>

    <label for="method">Selecciona un modo de compra:</label><br>
    <select id="method">
      <option value="">-- Elige una opción --</option>
      <option value="Yape">Yape</option>
      <option value="Plin">Plin</option>
      <option value="Contra entrega">Contra entrega</option>
      <option value="Transferencia">Transferencia bancaria</option>
    </select><br>
    
    <button id="buyBtn" onclick="completePurchase()">Comprar</button>
    <p id="success"></p>
  </div>

  <script>
    const productos = [];
    for (let i = 1; i <= 50; i++) {
      productos.push({
        nombre: "Producto Artesanal " + i,
        precio: (Math.random() * 40 + 10).toFixed(2),
        imagen: "https://via.placeholder.com/200x120?text=Artesania+" + i
      });
    }

    const productGrid = document.getElementById("productGrid");
    const cartItems = document.getElementById("cartItems");
    const totalSpan = document.getElementById("total");
    const successMessage = document.getElementById("success");
    let carrito = [];

    function mostrarProductos() {
      productos.forEach((producto, index) => {
        const div = document.createElement("div");
        div.className = "product";
        div.innerHTML = `
          <img src="${producto.imagen}" alt="${producto.nombre}">
          <h3>${producto.nombre}</h3>
          <p>Precio: S/ ${producto.precio}</p>
          <button onclick="agregarAlCarrito(${index})">Agregar</button>
        `;
        productGrid.appendChild(div);
      });
    }

    function agregarAlCarrito(index) {
      carrito.push(productos[index]);
      actualizarCarrito();
    }

    function actualizarCarrito() {
      cartItems.innerHTML = "";
      let total = 0;
      carrito.forEach((prod, i) => {
        total += parseFloat(prod.precio);
        const li = document.createElement("li");
        li.textContent = `${prod.nombre} - S/ ${prod.precio}`;
        cartItems.appendChild(li);
      });
      totalSpan.textContent = total.toFixed(2);
    }

    function completePurchase() {
      const metodo = document.getElementById("method").value;
      if (carrito.length === 0) {
        alert("El carrito está vacío.");
        return;
      }
      if (!metodo) {
        alert("Por favor, selecciona un método de compra.");
        return;
      }

      // Simulación de compra
      successMessage.textContent = `¡Compra realizada con éxito por ${metodo}! Gracias por confiar en Happy. 🎉`;
      carrito = [];
      actualizarCarrito();
      document.getElementById("method").value = "";
    }

    mostrarProductos();
  </script>

</body>
</html>
