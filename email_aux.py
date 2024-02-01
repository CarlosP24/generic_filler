def write_text(name, guardian_name, center_cat):
    text = '''
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="left">
                        <p style="width:650px;">
                            ¡Hola {gn}!
                            <br> Queremos confirmarte que la inscripción a la Prepascua 2024 (15 a 17 de marzo) de {n} ha sido realizada con éxito. 
                            Adjunta encontrarás la autorización que debes imprimir o solicitar impresa en tu centro, firmar y entregar como tarde el día de la actividad. Recuerda que es imprescindible para poder participar.
                            La persona responsable de {n} durante la convivencia será {cc}. Si no tienes su contacto puedes pedirlo en tu centro de JMV.
                            Además, puedes unirte al canal de WhatsApp para familiares de participantes en <a href="https://chat.whatsapp.com/IRwa34YMR57Jkzk2PNvm8Q">este enlace</a>.
                            Nos vemos el día 15 de marzo a las 18:00 en <a href="https://maps.app.goo.gl/59Dwre6TKvULsRbo6">calle Bailén, 43</a>.
                            Muchas gracias,
                            <br> El equipo organizador de la Prepascua
                            JMV - Área 12+9
                            <br>"Sencillamente, entrégate."
                        </p>
                    </td>
                </tr>
            </table>
            '''.format(gn = guardian_name, n = name, cc = center_cat)
    return text