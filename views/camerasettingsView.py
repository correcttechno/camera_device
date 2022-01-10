from views.mainView import MainView


def CameraSettingsView():


    PAGE= """
	<div class="page-wrapper">
    <div class="page-content">

		<div class="row">
			<div class="col-xl-12 col-12 mx-auto">
				<h6 class="mb-0 text-uppercase">Camera Settings</h6>
				<hr/>
			</div>

			<div class="col-xl-12 col-12">
				<div class="row">
					<div class="col-lg-6 col-12">
						<div class="form-group">
							Select View
							<select class="form-control" id="display_mode">
								<option value="normal">Normal</option>
								<option value="edged">Edged</option>
							</select>
						</div>
						<div class="form-group">
							Draw Rectange
							<select class="form-control" id="draw_rectangle">
								<option value="normal">On</option>
								<option value="edged">Off</option>
							</select>
						</div>
						<div class="form-group">
							Countr Value
							<select class="form-control" id="draw_rectangle">
								<option value="300">300</option>
								<option value="350">350</option>
								<option value="400">400</option>
								<option value="450">450</option>
								<option value="500">500</option>
								<option value="550">550</option>
								<option value="600">600</option>
								<option value="650">650</option>
							</select>
						</div>
					</div>
					<div class="col-lg-6 col-12">
						<img id="_stream" class="live-screen sc-screen" alt="Loading..." />
					</div>
				</div>
			</div>

		</div>

    </div>
	</div>"""
    return MainView(PAGE)