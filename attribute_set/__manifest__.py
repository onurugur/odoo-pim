{
    "name": "Attribute Set",
    "version": "17.0.1.0.0",
    "category": "Generic Modules/Others",
    "license": "AGPL-3",
    "author": "OnurUgur,Akretion,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/odoo-pim",
    "depends": ["base", "base_sparse_field"],
    "data": [
        "security/ir.model.access.csv",
        "security/attribute_security.xml",
        "views/menu_view.xml",
        "views/attribute_attribute_view.xml",
        "views/attribute_group_view.xml",
        "views/attribute_option_view.xml",
        "views/attribute_set_view.xml",
        "wizard/attribute_option_wizard_view.xml",
    ],
    "external_dependencies":
        {"python":
             ["unidecode"]
        },
    "installable": True,
}
