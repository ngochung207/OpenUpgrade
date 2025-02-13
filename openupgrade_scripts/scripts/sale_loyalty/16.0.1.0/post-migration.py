from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "sale_loyalty", "16.0.1.0/noupdate_changes.xml")
    openupgrade.delete_records_safely_by_xml_id(
        env,
        [
            "sale_coupon.sale_coupon_apply_code_rule",
            "sale_coupon.mail_template_sale_coupon",
        ],
    )
