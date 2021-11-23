from views.mainView import MainView


def WhitelistaddView():
    PAGE= """<div class="page-wrapper">
			<div class="page-content">
				
				<div class="row">
					<div class="col-xl-9 mx-auto">
						<h6 class="mb-0 text-uppercase">ADD Plate</h6>
						<hr/>
						<div class="card">
							<div class="card-body">
                                <label>Plate</label>
								<input id="lisence_plate" class="form-control mb-3" type="text" placeholder="Car Lisence Plate" aria-label="default input example">
                                <button id="save_plate" class="btn btn-light">Save</button>
							</div>
						</div>
						
					</div>
				</div>
				<!--end row-->
			</div>
		</div>"""
    return MainView(PAGE)