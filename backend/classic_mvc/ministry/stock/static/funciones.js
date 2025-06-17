



////////////////////////////////Funciones para RQ////////////////////////////

 // JavaScript para mostrar/ocultar la lista de entradas individuales
 const toggleButtons = document.querySelectorAll('.toggle-button');
 toggleButtons.forEach(button => {
   button.addEventListener('click', () => {
     const entradaList = button.nextElementSibling;
     if (entradaList.style.display === 'none' || entradaList.style.display === '') {
       entradaList.style.display = 'block';
     } else {
       entradaList.style.display = 'none';
     }
   });
 });
 
 // Aca empieza el carrito =-\
 const carrito = {};
 
 // Agregar un producto al carrito
 function agregarAlCarrito(productoNombre, fechaVencimiento, cantidadAgregar) {
   const clave = `${productoNombre}-${fechaVencimiento}`;
   if (carrito.hasOwnProperty(clave)) {
     // Si el producto ya existe en el carrito, actualiza la cantidad
     carrito[clave].cantidad += cantidadAgregar;
   } else {
     // Si el producto no existe, crea un nuevo elemento en el carrito
     carrito[clave] = {
       productoNombre,
       fechaVencimiento,
       cantidad: cantidadAgregar,
     };
   }
 }
 
 // Función para actualizar el contenido del carrito en la página
 function actualizarCarrito() {
   const carritoList = document.getElementById('carrito-list');
   // Limpiar contenido anterior
   carritoList.innerHTML = '';
 
   // Recorrer el carrito y agregar elementos al carrito
   for (const clave in carrito) {
     if (carrito.hasOwnProperty(clave)) {
       const producto = carrito[clave];
       const listItem = document.createElement('li');
       listItem.textContent = `${producto.cantidad} unidades de ${producto.productoNombre} (Vencimiento: ${producto.fechaVencimiento})`;
       listItem.setAttribute('data-producto', producto.productoNombre);
       listItem.setAttribute('data-fecha', producto.fechaVencimiento);
       listItem.setAttribute('data-cantidad', producto.cantidad);
       carritoList.appendChild(listItem);
     }
   }
 }
 
 // Agregar productos al carrito y actualizar la cantidad
 const agregarBotones = document.querySelectorAll('.agregar-producto');
 const carritoList = document.getElementById('carrito-list');
 
 agregarBotones.forEach(boton => {
   boton.addEventListener('click', () => {
     const productoNombre = boton.getAttribute('data-producto');
     const fechaVencimiento = boton.getAttribute('data-fecha');
     const cantidadOriginalInput = boton.parentElement.querySelector('.cantidad-original');
     const cantidadDuplicadaSpan = boton.parentElement.querySelector('.cantidad-duplicada');
     const cantidadInput = boton.parentElement.querySelector('#cantidad-agregar');
     const cantidadAgregar = parseInt(cantidadInput.value);
     const cantidadOriginal = parseInt(cantidadOriginalInput.value);
 
     if (cantidadAgregar > 0 && cantidadAgregar <= cantidadOriginal) {
 
       // Resta la cantidad agregada de la cantidad original y actualiza
       const nuevaCantidad = cantidadOriginal - cantidadAgregar;
       cantidadOriginalInput.value = nuevaCantidad; // Actualiza el valor en el campo oculto
       cantidadDuplicadaSpan.textContent = nuevaCantidad; // Actualiza el valor mostrado
 
       // Agrega el producto al carrito llamando a la función
       agregarAlCarrito(productoNombre, fechaVencimiento, cantidadAgregar);
 
       // Muestra el contenido actualizado del carrito
       actualizarCarrito();
 
       alert(`Agregado al carrito: ${cantidadAgregar} unidades de ${productoNombre}`);
     } else if (cantidadAgregar <= 0) {
       alert('La cantidad debe ser mayor que 0.');
     } else {
       alert(`La cantidad no puede ser mayor que ${cantidadOriginal}.`);
     }
   });
 });
 
 
 // Eliminar un producto del carrito
 const eliminarProductoButton = document.getElementById('eliminar-producto');
 eliminarProductoButton.addEventListener('click', () => {
   const carritoList = document.getElementById('carrito-list');
   const selectedProduct = carritoList.querySelector('.selected'); // Obtener el elemento seleccionado
 
   if (selectedProduct) {
     const productoNombre = selectedProduct.getAttribute('data-producto');
     const fechaVencimiento = selectedProduct.getAttribute('data-fecha');
     const cantidad = parseInt(selectedProduct.getAttribute('data-cantidad'));
 
     // Eliminar el producto del carrito
     const clave = `${productoNombre}-${fechaVencimiento}`;
     if (carrito.hasOwnProperty(clave)) {
       const cantidadEliminada = carrito[clave].cantidad;
 
       delete carrito[clave];
       
     
 
       // Actualizar la vista del carrito
       carritoList.removeChild(selectedProduct);
       actualizarCarrito();
       alert(`Producto ${productoNombre} eliminado del carrito.`);
     }
   } else {
     alert('Selecciona un producto en el carrito para eliminarlo.');
   }
 });
 
 // Reducir la cantidad de un producto en el carrito
 const reducirCantidadButton = document.getElementById('reducir-cantidad');
 reducirCantidadButton.addEventListener('click', () => {
   const carritoList = document.getElementById('carrito-list');
   const selectedProduct = carritoList.querySelector('.selected'); // Obtener el elemento seleccionado
 
   if (selectedProduct) {
     const productoNombre = selectedProduct.getAttribute('data-producto');
     const fechaVencimiento = selectedProduct.getAttribute('data-fecha');
     const cantidad = parseInt(selectedProduct.getAttribute('data-cantidad'));
 
     // Reducir la cantidad del producto en el carrito
     const clave = `${productoNombre}-${fechaVencimiento}`;
     if (carrito.hasOwnProperty(clave) && carrito[clave].cantidad > 1) {
       carrito[clave].cantidad--;
 
       // Actualizar la vista del carrito
       carritoList.removeChild(selectedProduct);
       selectedProduct.setAttribute('data-cantidad', carrito[clave].cantidad);
       selectedProduct.textContent = `${carrito[clave].cantidad} unidades de ${productoNombre} (Vencimiento: ${fechaVencimiento})`;
       carritoList.appendChild(selectedProduct);
 
       alert(`Cantidad de ${productoNombre} reducida en el carrito.`);
     }
   } else {
     alert('Selecciona un producto en el carrito para reducir su cantidad.');
   }
 });
 
 document.addEventListener('DOMContentLoaded', function () {

    // Seleccionar un producto en el carrito
    const carritoList = document.getElementById('carrito-list');
  
    carritoList.addEventListener('click', (event) => {
      const selectedItem = event.target;
      if (selectedItem && selectedItem.nodeName === 'LI') {
        // Cambia el estado de selección del producto
        const isSelected = selectedItem.getAttribute('data-selected') === 'true';
        selectedItem.setAttribute('data-selected', !isSelected);
  
        // Cambia el estilo para resaltar o deseleccionar el producto
        if (!isSelected) {
          selectedItem.classList.add('selected');
        } else {
          selectedItem.classList.remove('selected');
        }
      }
    });
  
    // Agregar un listener al botón "confirmar compra" en createrq para mostrar el carrito
    const confirmarButtonCreaterq = document.getElementById('confirmar-button'); // Asegúrate de que el ID sea correcto
    confirmarButtonCreaterq.addEventListener('click', (e) => {
      e.preventDefault(); // Evita que se realice el envío del formulario
      
      // Almacenar los datos del carrito en localStorage
      localStorage.setItem('carrito', JSON.stringify(carrito));
      

  
      // Redirigir al usuario a la página createrq
      window.location.href = '/createrq'; // Asegúrate de que esta sea la ruta correcta
    });
  });
  
 
 
 
 









// const confirmarButton = document.getElementById('confirmar-compra');
//   confirmarButton.addEventListener('click', () => {
//     // Aquí puedes realizar cualquier acción adicional antes de mostrar el formulario de remito.

//     // Luego, muestra el formulario de remito llamando a la función
//     mostrarFormularioRemito();
//   });

//   function mostrarFormularioRemito() {
//     // Oculta la pantalla inicial
//     const pantallaInicial = document.getElementById('pantalla-inicial');
//     pantallaInicial.style.display = 'none';

//     // Muestra el formulario de remito
//     const formularioRemito = document.getElementById('formulario-remito');
//     formularioRemito.style.display = 'block';
//   }
      
      
      
//        // JavaScript para mostrar/ocultar la lista de entradas individuales
//       const toggleButtons = document.querySelectorAll('.toggle-button');
//       toggleButtons.forEach(button => {
//         button.addEventListener('click', () => {
//           const entradaList = button.nextElementSibling;
//           if (entradaList.style.display === 'none' || entradaList.style.display === '') {
//             entradaList.style.display = 'block';
//           } else {
//             entradaList.style.display = 'none';
//           }
//         });
//       });
      
//       // Estructura de datos para el carrito
//       const carrito = {};
      
//       // Función para agregar un producto al carrito
//       function agregarAlCarrito(productoNombre, fechaVencimiento, cantidadAgregar) {
//         const clave = `${productoNombre}-${fechaVencimiento}`;
//         if (carrito.hasOwnProperty(clave)) {
//           // Si el producto ya existe en el carrito, actualiza la cantidad
//           carrito[clave].cantidad += cantidadAgregar;
//         } else {
//           // Si el producto no existe, crea un nuevo elemento en el carrito
//           carrito[clave] = {
//             productoNombre,
//             fechaVencimiento,
//             cantidad: cantidadAgregar,
//           };
//         }
//       }
      
//       // Función para actualizar el contenido del carrito en la página
//       function actualizarCarrito() {
//         const carritoList = document.getElementById('carrito-list');
//         // Limpiar contenido anterior
//         carritoList.innerHTML = '';
      
//         // Recorrer la estructura del carrito y agregar elementos al carrito
//         for (const clave in carrito) {
//           if (carrito.hasOwnProperty(clave)) {
//             const producto = carrito[clave];
//             const listItem = document.createElement('li');
//             listItem.textContent = `${producto.cantidad} unidades de ${producto.productoNombre} (Vencimiento: ${producto.fechaVencimiento})`;
//             listItem.setAttribute('data-producto', producto.productoNombre);
//             listItem.setAttribute('data-fecha', producto.fechaVencimiento);
//             listItem.setAttribute('data-cantidad', producto.cantidad);
//             carritoList.appendChild(listItem);
//           }
//         }
//       }
      
//       // JavaScript para agregar productos al carrito y actualizar la cantidad
//       const agregarBotones = document.querySelectorAll('.agregar-producto');
//       const carritoList = document.getElementById('carrito-list');
      
//       agregarBotones.forEach(boton => {
//         boton.addEventListener('click', () => {
//           const productoNombre = boton.getAttribute('data-producto');
//           const fechaVencimiento = boton.getAttribute('data-fecha');
//           const cantidadOriginalInput = boton.parentElement.querySelector('.cantidad-original');
//           const cantidadDuplicadaSpan = boton.parentElement.querySelector('.cantidad-duplicada');
//           const cantidadInput = boton.parentElement.querySelector('#cantidad-agregar');
//           const cantidadAgregar = parseInt(cantidadInput.value);
//           const cantidadOriginal = parseInt(cantidadOriginalInput.value);
      
//           if (cantidadAgregar > 0 && cantidadAgregar <= cantidadOriginal) {
//             // Resta la cantidad agregada de la cantidad original y actualiza
//             const nuevaCantidad = cantidadOriginal - cantidadAgregar;
//             cantidadOriginalInput.value = nuevaCantidad; // Actualiza el valor en el campo oculto
//             cantidadDuplicadaSpan.textContent = nuevaCantidad; // Actualiza el valor mostrado
      
//             // Agrega el producto al carrito llamando a la función
//             agregarAlCarrito(productoNombre, fechaVencimiento, cantidadAgregar);
      
//             // Muestra el contenido actualizado del carrito
//             actualizarCarrito();
      
//             alert(`Agregado al carrito: ${cantidadAgregar} unidades de ${productoNombre}`);
//           } else if (cantidadAgregar <= 0) {
//             alert('La cantidad debe ser mayor que 0.');
//           } else {
//             alert(`La cantidad no puede ser mayor que ${cantidadOriginal}.`);
//           }
//         });
//       });
      
//       // JavaScript para eliminar un producto del carrito
//       const eliminarProductoButton = document.getElementById('eliminar-producto');
//       eliminarProductoButton.addEventListener('click', () => {
//         const carritoList = document.getElementById('carrito-list');
//         const selectedProduct = carritoList.querySelector('.selected'); // Obtener el elemento seleccionado
      
//         if (selectedProduct) {
//           const productoNombre = selectedProduct.getAttribute('data-producto');
//           const fechaVencimiento = selectedProduct.getAttribute('data-fecha');
//           const cantidad = parseInt(selectedProduct.getAttribute('data-cantidad'));
      
//           // Eliminar el producto del carrito
//           const clave = `${productoNombre}-${fechaVencimiento}`;
//           if (carrito.hasOwnProperty(clave)) {
//             delete carrito[clave];
      
//             // Actualizar la vista del carrito
//             carritoList.removeChild(selectedProduct);
//             actualizarCarrito();
//             alert(`Producto ${productoNombre} eliminado del carrito.`);
//           }
//         } else {
//           alert('Selecciona un producto en el carrito para eliminarlo.');
//         }
//       });
      
//       // JavaScript para reducir la cantidad de un producto en el carrito
//       const reducirCantidadButton = document.getElementById('reducir-cantidad');
//       reducirCantidadButton.addEventListener('click', () => {
//         const carritoList = document.getElementById('carrito-list');
//         const selectedProduct = carritoList.querySelector('.selected'); // Obtener el elemento seleccionado
      
//         if (selectedProduct) {
//           const productoNombre = selectedProduct.getAttribute('data-producto');
//           const fechaVencimiento = selectedProduct.getAttribute('data-fecha');
//           const cantidad = parseInt(selectedProduct.getAttribute('data-cantidad'));
      
//           // Reducir la cantidad del producto en el carrito
//           const clave = `${productoNombre}-${fechaVencimiento}`;
//           if (carrito.hasOwnProperty(clave) && carrito[clave].cantidad > 1) {
//             carrito[clave].cantidad--;
      
//             // Actualizar la vista del carrito
//             carritoList.removeChild(selectedProduct);
//             selectedProduct.setAttribute('data-cantidad', carrito[clave].cantidad);
//             selectedProduct.textContent = `${carrito[clave].cantidad} unidades de ${productoNombre} (Vencimiento: ${fechaVencimiento})`;
//             carritoList.appendChild(selectedProduct);
      
//             alert(`Cantidad de ${productoNombre} reducida en el carrito.`);
//           }
//         } else {
//           alert('Selecciona un producto en el carrito para reducir su cantidad.');
//         }
//       });
      
//       document.addEventListener('DOMContentLoaded', function () {
//         // ...
      
//         // JavaScript para seleccionar un producto en el carrito
//         const carritoList = document.getElementById('carrito-list');
        
//         carritoList.addEventListener('click', (event) => {
//           const selectedItem = event.target;
//           if (selectedItem && selectedItem.nodeName === 'LI') {
//             // Cambia el estado de selección del producto
//             const isSelected = selectedItem.getAttribute('data-selected') === 'true';
//             selectedItem.setAttribute('data-selected', !isSelected);
            
//             // Cambia el estilo para resaltar o deseleccionar el producto
//             if (!isSelected) {
//               selectedItem.classList.add('selected');
//             } else {
//               selectedItem.classList.remove('selected');
//             }
//           }
//         });
      
//         // ...
//       });

//     document.getElementById('remito-form').addEventListener('submit', function (e) {
//     e.preventDefault(); // Evita que el formulario se envíe normalmente

//     // Obtiene los valores de los campos del formulario
//     const nombreDestinatario = document.getElementById('nombre-destinatario').value;
//     const direccionDestinatario = document.getElementById('direccion-destinatario').value;

//     // Construye la URL con los datos del formulario
//     //const url = `/createrq/?nombre=${encodeURIComponent(nombreDestinatario)}&direccion=${encodeURIComponent(direccionDestinatario)}`;
//     const url = '/createrq'
//     // Redirige al usuario a la nueva página
//     window.location.href = url;
//   });


     

// ///