from nicegui import ui
ui.add_head_html('<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>')



async def showmyalert():
	await ui.run_javascript('''
		Swal.fire(
  'Good job!',
  'You clicked the button!',
  'success'
)

		''',respond=False)



async def showdangeralert():
	await ui.run_javascript('''
	Swal.fire({
  icon: 'error',
  title: 'Oops...',
  text: 'Something went wrong!',
  footer: '<a href="">Why do I have this issue?</a>'
})

		''',respond=False)
async def showhtmlalert():
	await ui.run_javascript('''
Swal.fire({
  title: '<strong>HTML <u>example</u></strong>',
  icon: 'info',
  html:
    'You can use <b>bold text</b>, ' +
    '<a href="//sweetalert2.github.io">links</a> ' +
    'and other HTML tags',
  showCloseButton: true,
  showCancelButton: true,
  focusConfirm: false,
  confirmButtonText:
    '<i class="fa fa-thumbs-up"></i> Great!',
  confirmButtonAriaLabel: 'Thumbs up, great!',
  cancelButtonText:
    '<i class="fa fa-thumbs-down"></i>',
  cancelButtonAriaLabel: 'Thumbs down'
})

		''',respond=False)


# CREATE BUTtoN FOR SHOW ALErt
ui.button("show alert",on_click=showmyalert)
ui.button("show ERROR ALERT",on_click=showdangeralert).classes("bg-red")
ui.button("show HTML",on_click=showhtmlalert)

ui.run(native=True)
