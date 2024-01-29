def write_text(name, guardian_name, center_cat):
    text = '''
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="left">
                        <p style="width:650px;">
                            ¡Hola {guardian_name}!
                            <br> Queremos confirmarte que la inscripción a la Prepascua 2024 (15 a 17 de marzo) de {name} ha sido realizada con éxito. 
                            Adjunta encontrarás la autorización que debes imprimir o solicitar impresa en tu centro, firmar y entregar como tarde el día de la actividad. Recuerda que es imprescindible para poder participar.
                            La persona responsable de {name} durante la convivencia será {center_cat}. Si no tienes su contacto puedes pedirlo en tu centro de JMV.
                            Además, puedes unirte al grupo de WhatsApp de familiares de los participantes en <a href="">este enlace</a>.
                            Nos vemos el día 15 a las 18:00 en Puerta de Toledo.
                            Muchas gracias,
                            <br> El equipo preparador de la Prepascua
                            JMV - Área 12+9
                            <br>"Sencillamente, entrégate."
                        </p>
                    </td>
                </tr>
            </table>
            '''.format(guardian_name, name, center_cat)
    return text