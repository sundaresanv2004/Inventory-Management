import flet as ft

from Main.functions.snack_bar import snack_bar1
from Main.pages.product import display_products
from Main.service.connection.mysql_connection import display_product, edit_product

alertdialog = ft.AlertDialog(modal=True)


def edit_product_page(page: ft.Page, index):
    global alertdialog

    def on_close(e):
        alertdialog.open = False
        page.update()

    data = display_product()

    def on_save(e):
        if category_dropdown.value is not None:
            category_dropdown.error_text = None
            category_dropdown.update()
            if name_dropdown.value is not None:
                name_dropdown.error_text = None
                name_dropdown.update()
                if len(str(quantity_entry.value)) != 0:
                    quantity_entry.error_text = None
                    quantity_entry.update()
                    if len(str(price_entry.value)) != 0:
                        price_entry.error_text = None
                        price_entry.update()
                        edit_product([int(data.loc[index].values[0]), str(quantity_entry.value), str(price_entry.value)])
                        on_close('e')
                        snack_bar1(page, "Updated Successfully!")
                        display_products(page)
                    else:
                        price_entry.error_text = "Enter the Price!"
                        price_entry.focus()
                        price_entry.update()
                else:
                    quantity_entry.error_text = "Enter the Quantity!"
                    quantity_entry.focus()
                    quantity_entry.update()
            else:
                name_dropdown.error_text = "Choose the Name!"
                name_dropdown.update()
        else:
            category_dropdown.error_text = "Choose Category!"
            category_dropdown.update()

    main_text = ft.Text(
        value="Edit Product",
        weight=ft.FontWeight.BOLD,
        size=25,
        font_family='Verdana',
    )

    category_dropdown = ft.Dropdown(
        hint_text="Category",
        text_style=ft.TextStyle(font_family='Verdana'),
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        color=ft.colors.BLACK,
        options=[
            ft.dropdown.Option("Fruits"),
            ft.dropdown.Option("Vegetables"),
        ],
        value=data.loc[index].values[1],
        prefix_icon=ft.icons.CATEGORY_ROUNDED,
        disabled=True,
    )

    name_dropdown = ft.Dropdown(
        hint_text="Category",
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        options=[
            ft.dropdown.Option(data.loc[index].values[2])
        ],
        value=data.loc[index].values[2],
        color=ft.colors.BLACK,
        prefix_icon=ft.icons.CATEGORY_ROUNDED,
        disabled=True
    )

    quantity_entry = ft.TextField(
        hint_text="Quantity",
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        value=data.loc[index].values[3],
        prefix_icon=ft.icons.PRODUCTION_QUANTITY_LIMITS_ROUNDED,
    )

    price_entry = ft.TextField(
        hint_text="Price",
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        value=data.loc[index].values[4],
        prefix_icon=ft.icons.CURRENCY_RUPEE_ROUNDED,
    )

    content = ft.Column(
        [
            category_dropdown,
            name_dropdown,
            quantity_entry,
            price_entry
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=500,
        height=390,
    )

    alertdialog.content = ft.Column(
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
        alignment=ft.MainAxisAlignment.START,
        width=500,
        height=390,
    )

    alertdialog.actions = [
        ft.TextButton(
            text="Save",
            on_click=on_save,
        ),
        ft.TextButton(
            text="Cancel",
            on_click=on_close,
        )
    ]

    alertdialog.actions_alignment = ft.MainAxisAlignment.END

    page.dialog = alertdialog
    alertdialog.open = True
    page.update()
