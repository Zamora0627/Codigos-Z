private void button1_Click(object sender, EventArgs e)
{
    int totalUnidades = int.Parse(txtTotalUnidades.Text);
    int gananciaTotal = int.Parse(txtGananciaTotal.Text);
    int precioTableta = int.Parse(txtPrecioTableta.Text);
    int precioLaptop = int.Parse(txtPrecioLaptop.Text);

    (int tabletasVendidas, int laptopsVendidas)? resultados = CalcularVentas(totalUnidades, gananciaTotal, precioTableta, precioLaptop);

    if (resultados.HasValue)
    {
        lblTabletasVendidas.Text = $"Tabletas vendidas: {resultados.Value.tabletasVendidas}";
        lblLaptopsVendidas.Text = $"Laptops vendidas: {resultados.Value.laptopsVendidas}";
    }
    else
    {
        MessageBox.Show("NO SE PUDO SOLUCIONAR CON LOS DATOS DADOS.");
    }
}

private (int, int)? CalcularVentas(int totalUnidades, int gananciaTotal, int precioTableta, int precioLaptop)
{
    for (int y = 0; y <= totalUnidades; y++)
    {
        int x = totalUnidades - y;
        if (precioTableta * x + precioLaptop * y == gananciaTotal)
        {
            return (x, y);
        }
    }
    return null;
}
