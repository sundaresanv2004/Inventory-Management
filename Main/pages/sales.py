import flet as ft

from Main.service.connection.mysql_connection import display_sales, display_product_by_id

table = ft.DataTable(
    column_spacing=50,
    columns=[
        ft.DataColumn(ft.Text("Sales ID")),
        ft.DataColumn(ft.Text("Product ID")),
        ft.DataColumn(ft.Text("Product Name")),
        ft.DataColumn(ft.Text("Product Category")),
        ft.DataColumn(ft.Text("Date")),
        ft.DataColumn(ft.Text("Total Amount")),

    ]
)


def sales_page(page: ft.Page, main_colum: ft.Column):
    global table

    def page_resize(e):
        table.width = page.width - 10
        page.update()

    table.width = page.width - 10

    main_colum.controls = [
        ft.Column(
            [
                table
            ],
            scroll=ft.ScrollMode.ADAPTIVE,
        )
    ]

    page.on_resize = page_resize

    page.splash = None
    page.update()
    display_sale(page)


def display_sale(page: ft.Page):
    data = display_sales()

    data_list = []
    if data.empty is False:
        for i in range(len(data)):
            temp = data.loc[i].values
            temp1 = display_product_by_id(int(temp[1]))
            data_list.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(temp[0])),
                        ft.DataCell(ft.Text(temp[1])),
                        ft.DataCell(ft.Text(temp1[2])),
                        ft.DataCell(ft.Text(temp1[1])),
                        ft.DataCell(ft.Text(temp[2])),
                        ft.DataCell(ft.Text(temp[3])),
                    ],
                ),
            )

    table.rows = data_list
    page.update()
