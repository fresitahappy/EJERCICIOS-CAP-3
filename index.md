<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Happy - Artesanías</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #fffdf7;
      margin: 0;
      padding: 20px;
    }
    h1, h2 {
      text-align: center;
      color: #d35400;
    }
    .hidden { display: none; }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 15px;
      margin-top: 30px;
    }
    .product {
      background: white;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 10px;
      text-align: center;
    }
    .product img {
      width: 100%;
      height: 120px;
      object-fit: cover;
      border-radius: 5px;
    }
    .product button {
      background: #e67e22;
      border: none;
      color: white;
      padding: 8px 12px;
      margin-top: 10px;
      border-radius: 5px;
      cursor: pointer;
    }
    .admin-controls input, .admin-controls button {
      margin-top: 5px;
      width: 90%;
      padding: 5px;
    }
    #cart {
      background: #f9f3e7;
      padding: 20px;
      border-radius: 10px;
      margin-top: 30px;
    }
    #cart ul { list-style: none; padding: 0; }
    #cart li { padding: 5px 0; }
    select, #buyBtn {
      padding: 10px;
      margin-top: 10px;
      font-size: 16px;
    }
    #success { color: green; text-align: center; margin-top: 20px; font-weight: bold; }
    #login { text-align: center; padding: 50px; }
    #login input, #login button {
      padding: 10px;
      font-size: 16px;
      margin: 5px;
    }
  </style>
</head>
<body>

  <div id="login">
    <h1>Bienvenido a Happy</h1>
    <p>¿Cómo deseas ingresar?</p>
    <button onclick="accederComoComprador()">Ingresar como Comprador</button><br><br>
    <input type="password" id="clave" placeholder="Contraseña profesional">
    <button onclick="verificarClave()">Ingresar como Profesional</button>
    <p id="error" style="color:red;"></p>
  </div>

  <div id="comprador" class="hidden">
    <h2>Productos disponibles</h2>
    <div class="grid" id="compradorProductos"></div>

    <div id="cart">
      <h2>Carrito de Compras</h2>
      <ul id="cartItems"></ul>
      <p><strong>Total: S/ <span id="total">0.00</span></strong></p>

      <label>Tipo de compra:</label>
      <select id="tipoCompra">
        <option value="">-- Elige tipo --</option>
        <option>Presencial (efectivo)</option>
        <option>Virtual (Yape, Plin, Transferencia)</option>
      </select><br>

      <button id="buyBtn" onclick="realizarCompra()">Realizar Compra</button>
      <p id="success"></p>
    </div>
  </div>

  <div id="profesional" class="hidden">
    <h2>Gestión de productos</h2>
    <div class="grid" id="adminProductos"></div>

    <h3>Agregar nuevo producto</h3>
    <div class="admin-controls">
      <input type="text" id="nuevoNombre" placeholder="Nombre del producto">
      <input type="text" id="nuevoPrecio" placeholder="Precio">
      <input type="text" id="nuevaImagen" placeholder="URL de imagen">
      <button onclick="agregarProducto()">Añadir Producto</button>
    </div>
  </div>

  <script>
    let productos = [];
    let carrito = [];

    // Cargar 50 productos por defecto
    for (let i = 1; i <= 50; i++) {
      productos.push({
        nombre: "Producto Artesanal " + i,
        precio: (Math.random() * 40 + 10).toFixed(2),
        imagen: "https://via.placeholder.com/200x120?text=Artesania+" + i
      });
    }

    function accederComoComprador() {
      document.getElementById("login").classList.add("hidden");
      document.getElementById("comprador").classList.remove("hidden");
      mostrarProductosComprador();
    }

    function verificarClave() {
      const clave = document.getElementById("clave").value;
      if (clave === "happy123") {
        document.getElementById("login").classList.add("hidden");
        document.getElementById("profesional").classList.remove("hidden");
        mostrarProductosAdmin();
      } else {
        document.getElementById("error").textContent = "Contraseña incorrecta";
      }
    }

    // ----------------------- COMPRADOR ----------------------
    function mostrarProductosComprador() {
      const cont = document.getElementById("compradorProductos");
      cont.innerHTML = "";
      productos.forEach((p, i) => {
        const div = document.createElement("div");
        div.className = "product";
        div.innerHTML = `
          <img src="${p.imagen}" alt="${p.nombre}">
          <h4>${p.nombre}</h4>
          <p>S/ ${p.precio}</p>
          <button onclick="añadirAlCarrito(${i})">Añadir</button>
        `;
        cont.appendChild(div);
      });
    }

    function añadirAlCarrito(index) {
      carrito.push(productos[index]);
      actualizarCarrito();
    }

    function actualizarCarrito() {
      const lista = document.getElementById("cartItems");
      const totalTxt = document.getElementById("total");
      lista.innerHTML = "";
      let total = 0;
      carrito.forEach(p => {
        const li = document.createElement("li");
        li.textContent = `${p.nombre} - S/ ${p.precio}`;
        lista.appendChild(li);
        total += parseFloat(p.precio);
      });
      totalTxt.textContent = total.toFixed(2);
    }

    function realizarCompra() {
      const tipo = document.getElementById("tipoCompra").value;
      if (!tipo) {
        alert("Selecciona el tipo de compra.");
        return;
      }
      if (carrito.length === 0) {
        alert("El carrito está vacío.");
        return;
      }
      document.getElementById("success").textContent = `¡Compra realizada como ${tipo}! Gracias por tu pedido 🎉`;
      carrito = [];
      actualizarCarrito();
      document.getElementById("tipoCompra").value = "";
    }

    // ----------------------- PROFESIONAL ----------------------

    function mostrarProductosAdmin() {
      const cont = document.getElementById("adminProductos");
      cont.innerHTML = "";
      productos.forEach((p, i) => {
        const div = document.createElement("div");
        div.className = "product";
        div.innerHTML = `
          <img src="${p.imagen}" alt="${p.nombre}">
          <input type="text" value="${p.nombre}" onchange="editarProducto(${i}, 'nombre', this.value)">
          <input type="text" value="${p.precio}" onchange="editarProducto(${i}, 'precio', this.value)">
          <input type="text" value="${p.imagen}" onchange="editarProducto(${i}, 'imagen', this.value)">
          <button onclick="eliminarProducto(${i})">Eliminar</button>
        `;
        cont.appendChild(div);
      });
    }

    function editarProducto(index, campo, valor) {
      productos[index][campo] = valor;
      mostrarProductosAdmin();
    }

    function eliminarProducto(index) {
      if (confirm("¿Eliminar este producto?")) {
        productos.splice(index, 1);
        mostrarProductosAdmin();
      }
    }

    function agregarProducto() {
      const nombre = document.getElementById("nuevoNombre").value.trim();
      const precio = document.getElementById("nuevoPrecio").value.trim();
      const imagen = document.getElementById("nuevaImagen").value.trim();

      if (!nombre || !precio || !imagen) {
        alert("Rellena todos los campos.");
        return;
      }
      productos.push({ nombre, precio, imagen });
      mostrarProductosAdmin();

      document.getElementById("nuevoNombre").value = "";
      document.getElementById("nuevoPrecio").value = "";
      document.getElementById("nuevaImagen").value = "";
    }
  </script>

</body>
</html>
