import flet as ft

from Main.functions.snack_bar import snack_bar1
from Main.pages.product import display_products
from Main.service.connection.mysql_connection import display_product, add_product

category_dict = {
    "Fruits": [
        "Apple",
        "Avocado",
        "Banana",
        "Coconut",
        "Grapes",
        "Guava",
        "Jackfruit",
        "Lemon",
        "Orange",
        "Sweet Potato",
        "Cucumber"
    ],
    "Vegetables": [
        "Potato",
        "Cabbage",
        "Tomato",
        "Cauliflower",
        "Brinjal",
        "Carrot",
        "Peas"
    ]
}

alertdialog = ft.AlertDialog(modal=True)
val_list_product = ["", "", "", "", ""]
temp = False


def add_product_page(page: ft.Page):
    global alertdialog, val_list_product, temp

    def on_close(e):
        global val_list_product, temp
        val_list_product = val_list_product = ["", "", "", "", ""]
        alertdialog.open = False
        temp = False
        page.update()

    def dropdown_change(e):
        name_dropdown.options = None
        for i in category_dict[category_dropdown.value]:
            name_dropdown.options.append(ft.dropdown.Option(i))
        page.update()

    def on_save(e):
        global temp, val_list_product
        if category_dropdown.value is not None:
            category_dropdown.error_text = None
            category_dropdown.update()
            if name_dropdown.value is not None:
                name_dropdown.error_text = None
                name_dropdown.update()
                if len(quantity_entry.value) != 0:
                    quantity_entry.error_text = None
                    quantity_entry.update()
                    if len(price_entry.value) != 0:
                        price_entry.error_text = None
                        price_entry.update()
                        data = display_product()
                        val_list_product[0] = category_dropdown.value
                        val_list_product[1] = name_dropdown.value
                        val_list_product[2] = quantity_entry.value
                        val_list_product[3] = price_entry.value
                        val_list_product[4] = str(name_dropdown.value).lower() + ".png"
                        if data[data.name == name_dropdown.value].empty:
                            add_product(val_list_product)
                            on_close('e')
                            snack_bar1(page, "Added Successfully!")
                            display_products(page)
                        else:
                            temp = True
                            alert(page)
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
        value="Add Product",
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
        prefix_icon=ft.icons.CATEGORY_ROUNDED,
        on_change=dropdown_change,
    )

    name_dropdown = ft.Dropdown(
        hint_text="Category",
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        color=ft.colors.BLACK,
        prefix_icon=ft.icons.CATEGORY_ROUNDED,
    )

    quantity_entry = ft.TextField(
        hint_text="Quantity",
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        prefix_icon=ft.icons.PRODUCTION_QUANTITY_LIMITS_ROUNDED,
    )

    price_entry = ft.TextField(
        hint_text="Price",
        width=400,
        border=ft.InputBorder.OUTLINE,
        border_radius=9,
        prefix_icon=ft.icons.CURRENCY_RUPEE_ROUNDED,
    )

    if len(val_list_product[0]) != 0:
        category_dropdown.value = val_list_product[0]
        dropdown_change('e')
        name_dropdown.value = val_list_product[1]
        quantity_entry.value = val_list_product[2]
        price_entry.value = val_list_product[3]

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
    if temp is False:
        alertdialog.open = True
    page.update()


def alert(page: ft.Page):
    def on_ok(e):
        alertdialog.title = None
        add_product_page(page)

    alertdialog.title = ft.Text("Already Exist!")
    alertdialog.content = ft.Text("Record already exist try editing it.")
    alertdialog.actions = [
        ft.TextButton(
            text="Ok",
            on_click=on_ok,
        ),
    ]
    page.update()
