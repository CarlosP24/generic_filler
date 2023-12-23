def write_text(name, guardian_name):
    text = '''
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="left">
                        <p style="width:650px;">
                            ¡Hola {}!
                            <br> Queremos confirmarte que la inscripción a la Vigilia de la Milagrosa (24 de noviembre) de {} ha sido realizada con éxito. 
                            Adjunta encontrarás la autorización que debes imprimir o solicitar impresa en tu centro, firmar y entregar el día de la actividad. Recuerda que es imprescindible para poder participar.
                            Muchas gracias,
                            <br> El equipo preparador de la Vigilia
                            JMV - Área 12
                            <br>"Sencillamente, entrégate."
                        </p>
                    </td>
                </tr>
            </table>
            '''.format(guardian_name, name)
    return text