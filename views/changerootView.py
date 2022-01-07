from views.mainView import MainView


def ChangeRootView():
    PAGE= """<div class="page-wrapper">
			<div class="page-content">
				
				<div class="row">
					<div class="col-xl-9 mx-auto">
						<h6 class="mb-0 text-uppercase">Change Root Password</h6>
						<hr/>
						<div class="card">
							<div class="card-body">
                                <label>Password</label>
								<input id="password" class="form-control mb-3" type="text" placeholder="Password" aria-label="default input example">
                                <label>Retry Password</label>
								<input id="retrypassword" class="form-control mb-3" type="text" placeholder="Retry Password" aria-label="default input example">
                                <div id="msg"></div>
                                <button id="save_password" class="btn btn-light">Save</button>
							</div>
						</div>
						
					</div>
				</div>
				<!--end row-->
			</div>
		</div>"""
    return MainView(PAGE)