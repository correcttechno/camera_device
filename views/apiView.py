from database import readApi
from views.mainView import MainView




def ApiView():


    request_url=''
    plate=''
    date=''
    scaned_image=''
    cropped_image=''

    for row in readApi():
        if(row[1]=='api_request_url'):
            request_url=row[2]
        elif(row[1]=='api_plate' and row[2]=='1'):
            plate='checked'
        elif(row[1]=='api_date' and row[2]=='1'):
            date='checked'
        elif(row[1]=='api_scaned_image' and row[2]=='1'):
            scaned_image='checked'
        elif(row[1]=='api_cropped_image' and row[2]=='1'):
            cropped_image='checked'
    PAGE= """<div class="page-wrapper">
			<div class="page-content">
				<h6 class="mb-0 text-uppercase">Api Integration</h6>
				<div class="row">
					<div class="col-xl-12 col-lg-12 mx-auto">
						<h6 class="mb-0 text-uppercase"></h6>
						<hr/>
						<div class="card">
							<div class="card-body">
                                <label>Request URL</label>
								<input id="request_url"  value='"""+request_url+"""' class="form-control mb-3" type="text" placeholder="http:// or https://" aria-label="default input example">
                                <p>Attach data for request</p>
                                <div ><label> <input """+plate+"""  type="checkbox" id="plate" value="1"/> Lisence Plate </label></div>
                                <div ><label> <input """+date+""" type="checkbox" id="date" value="1"//> Date  </label></div>
                                <div ><label> <input """+scaned_image+""" type="checkbox" id="scaned_image" value="1"//> Scaned Image  </label></div>
                                <div ><label> <input """+cropped_image+""" type="checkbox" id="cropped_image" value="1"//> Cropped Image </label></div>

                                <button id="save_api" class="btn btn-light">Save</button>
							</div>
						</div>
						
					</div>
				</div>
				<!--end row-->
			</div>
		</div>"""
    return MainView(PAGE)