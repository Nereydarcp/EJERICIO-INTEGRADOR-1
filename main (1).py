
Productos = [[1, "Maíz en grano", 285.55], [2, "Pepino", 334.72], [3, "Tomate verde00", 129.00]]

Ventas_productos = [[2,122], 
[1,89], 
[1,22], 
[3,48],
[1,75],
[3,322],
[2,95],
[1,148],
[1,83],
[3,100]]

#Entradas 
Cantidad_cajas_para_vender = int(input('Ingrese la cantidad total de cajas a vender: '))
ID_producto = int(input('Ingrese el ID del producto: '))

#Salidas 
for producto in Productos:
  if producto[0] == ID_producto:
    Ventas_productos.append([ID_producto, Cantidad_cajas_para_vender])
    print(f' El producto es: {producto[1]}')
    print(f' El precio por caja es: {producto[2]}')
    total = producto[2] * Cantidad_cajas_para_vender
    if Cantidad_cajas_para_vender <= 100:
      total += 1500 #costo de envio)
    total_cajas = 0
    for venta in Ventas_productos:
      total_cajas += venta[1]
      
    if total_cajas > 1500:
      descuento = total * 0.20
      total = total - descuento

    print(f'Aplica el descuento del 20%: {total_cajas > 1500:}')
    print(f'El total a pagar es: {round(total, 2)}')
    

