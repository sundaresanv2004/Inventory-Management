import flet as ft

from Main.functions.snack_bar import snack_bar1
from Main.pages.sales import display_sale
from Main.service.connection.mysql_connection import display_product_by_category, display_product_by_name, save_sales


def sales_product(page: ft.Page):
    def on_close(e):
        alter.open = False
        page.update()

    def dropdown_change(e):
        name_dropdown.options = None
        df = display_product_by_category(category_dropdown.value)
        temp_list = df['name'].values.tolist()
        for i in temp_list:
            name_dropdown.options.append(ft.dropdown.Option(i))
        page.update()

    main_text = ft.Text(
        value="New Sale",
        weight=ft.FontWeight.BOLD,
        size=25,
        font_family='Verdana',
    )

    def save(e):
        if int(quantity_entry.value) > 0:
            quantity_entry.error_text = "Quantity is 0!"
            quantity_entry.update()
            a = display_product_by_name(name_dropdown.value).values[0]
            save_sales([int(a[0]),
                       int(quantity_entry.value) * a[4],
                        a[3] - int(quantity_entry.value)])
            on_close(e)
            snack_bar1(page, "Added Successfully!")
            display_sale(page)
        else:
            quantity_entry.error_text = "Quantity is 0!"
            quantity_entry.update()

    category_dropdown = ft.Dropdown(
        hint_text="Category",
        text_style=ft.TextStyle(font_family='Verdana'),
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        color=ft.colors.BLACK,
        on_change=dropdown_change,
        options=[
            ft.dropdown.Option("Fruits"),
            ft.dropdown.Option("Vegetables"),
        ],
        prefix_icon=ft.icons.CATEGORY_ROUNDED,
    )

    def on_change_name(e):
        if name_dropdown.value is not None:
            quantity_entry.disabled = False
            minus.disabled = False
            plus.disabled = False
        else:
            quantity_entry.disabled = True
            minus.disabled = True
            plus.disabled = True
        page.update()
        change_quantity(e)

    name_dropdown = ft.Dropdown(
        hint_text="Category",
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        color=ft.colors.BLACK,
        prefix_icon=ft.icons.CATEGORY_ROUNDED,
        on_change=on_change_name,
    )

    def change_quantity(e):
        df1 = display_product_by_name(name_dropdown.value)

        if quantity_entry.value == '0':
            minus.disabled = True
        else:
            minus.disabled = False

        if int(quantity_entry.value) > int(df1.values[0][3]):
            quantity_entry.value = str(df1.values[0][3])
            plus.disabled = True
        else:
            plus.disabled = False

        price_entry.value = f"Total Amount:  ₹{int(quantity_entry.value) * df1.values[0][4]}"

        page.update()

    def minus_click(e):

        quantity_entry.value = str(int(quantity_entry.value) - 1)
        page.update()
        change_quantity(e)

    def plus_click(e):
        quantity_entry.value = str(int(quantity_entry.value) + 1)
        page.update()
        change_quantity(e)

    minus = ft.IconButton(ft.icons.REMOVE, on_click=minus_click, disabled=True)
    plus = ft.IconButton(ft.icons.ADD, on_click=plus_click, disabled=True)

    quantity_entry = ft.TextField(
        hint_text="Quantity",
        width=200,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        value='0',
        disabled=True,
        prefix_icon=ft.icons.PRODUCTION_QUANTITY_LIMITS_ROUNDED,
        on_change=change_quantity,
    )

    price_entry = ft.Text(
        "Total Amount:  ₹00.00",
        size=20,
    )

    content = ft.Column(
        [
            category_dropdown,
            name_dropdown,
            ft.Row(
                [
                    minus,
                    quantity_entry,
                    plus,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            price_entry
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=500,
        height=390,
    )

    alter = ft.AlertDialog(
        content=ft.Column(
            [
                ft.Row(
                    [
                        main_text,
                        ft.IconButton(
                            icon=ft.icons.CLOSE_ROUNDED,
                            tooltip="Close",
                            on_click=on_close,
                        )
                    ],
                    width=500,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                content
            ],
            width=500,
            height=400,
        ),

        actions=[
            ft.TextButton(
                text="Ok",
                on_click=save,
            ),
            ft.TextButton(
                text="Cancel",
                on_click=on_close,
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.dialog = alter
    alter.open = True
    page.update()
