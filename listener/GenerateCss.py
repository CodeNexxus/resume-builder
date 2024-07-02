class GenerateCss:
	def __init__(self):
		self.code_stack = []

	def generate_code(self):
		self.code_start()

		result = ""
		for code in self.code_stack:
			result += code

		return result

	def code_start(self):
		self.generate_container()

		self.generate_header()
		self.generate_base_info()
		self.generate_body()

		self.generate_h2()
		self.generate_profile()
		self.generate_background()

		self.generate_general()
		self.generate_snackbar()
		self.generate_go_top()

	def generate_container(self):
		temp_code = """.container {
    background-color: transparent;
    width: 75%;
    min-width: 50rem;
    min-height: 100%;
    height: fit-content !important;
    margin: 3rem 0;
    a:hover {
        color: skyblue;
    }
}"""
		self.code_stack.append(temp_code)

	def generate_header(self):
		temp_code = """
.header-name {
    width: 100%;
    height: 10rem;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: transparent;
    color: white;
    font: 50px bold;
    margin-left: 5rem;
}

.information {
    width: 100%;
    min-height: calc(100% - 10rem);
    display: flex;
    border-radius: 7px;
    /* overflow: hidden; */
}
"""
		self.code_stack.append(temp_code)

	def generate_base_info(self):
		temp_code = """.base-info {
    width: 30%;
    padding: 1rem;
    box-sizing: border-box;
}"""
		self.code_stack.append(temp_code)

	def generate_body(self):
		temp_code = ('body {'
					 '/* font-family: Verdana, Geneva, Tahoma, sans-serif; */'
					 'font-family: Arial, Helvetica, sans-serif;'
					 'background: linear-gradient(to bottom, #767d9c, #000);'
					 '}')

		self.code_stack.append(temp_code)

	def generate_h2(self):
		temp_code = ('h2{'
					 'margin: unset;'
					 '}')

		self.code_stack.append(temp_code)

	def generate_profile(self):
		temp_code = """.profile-img {
	    display: flex;
	    justify-content: center;
	    align-items: center;
	    padding: 20px 0;


	    img {
	        height: 15rem;
	        width: 15rem;
	        border-radius: 50%;
	        object-fit: cover;
	        overflow: hidden;
	    }
	}
	"""

		self.code_stack.append(temp_code)

	def generate_background(self):
		temp_code = """.background {
    			display: flex;
    			justify-content: center;
    			margin: 0;
    			background-attachment: fixed;
				}"""

		self.code_stack.append(temp_code)

	def generate_general(self):
		temp_code = """.t1 .base-info {
    background-color: #141E46;
    color: white;
}

.t2 .base-info {
    background-color: #2B2A4C;
    color: white;
}

.t3 .base-info {
    background-color: #454545;
    color: white;
}

/* new s */
.additional-info-title{
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 10px;
}

.additioan-info-titles-icon{
    width: 25px;
}

/* new e */


.additional-info {
    width: 70%;
    padding: 1rem;
    box-sizing: border-box;
}

.t1 .additional-info {
    background-color: #FFF5E0;
}

.t2 .additional-info {
    background-color: #EEE2DE;
}

.t3 .additional-info {
    background-color: #FFE6C7;
}

hr.rounded {
    border-top: 2px solid #bbb;
    border-radius: 1px;
}

.non-styled-list {
    margin-inline-start: 2rem;
}

.hard-skills {
    ul {
        gap: 2rem;
        display: flex;
    }
}


.additional-info-list{
    display: flex;
    column-gap: 100px;
    flex-wrap: wrap;
}

.additional-info-item , .info-title{
    display: flex;
    justify-content: flex-start;
    align-items: center;
    gap: 10px;
}

.rate-star{
    width: 20px;
}

.link-white{
    text-decoration: underline;
    color: #fff;
}

.link{
    text-decoration: underline;
    color: #000;
    font-weight: 900;
}

.text{
    font-weight: lighter;
    color: #6d6d6d;
    margin: 7px;
    /* width: 500px; */
    text-align: justify;
}

.projects , .educations{
    display: flex;
    gap: 1rem;
    flex-direction: column;
}

.info-item , .base-item{
    padding-top: 15px;
}

.base-info-icon{
    width: 30px;
}"""
		self.code_stack.append(temp_code)

	def generate_snackbar(self):
		temp_code = """
/* snack bar */

#email-snackbar , #phone-snackbar {
    visibility: hidden;
    min-width: 250px;
    margin-left: -125px;
    background-color: #767d9c;
    color: #fff;
    text-align: center;
    border-radius: 2px;
    padding: 16px;
    position: fixed;
    z-index: 1;
    left: 50%;
    bottom: 30px;
    border-radius: 3rem;
    font-size: 1rem;
  }

  #email-snackbar.show  , #phone-snackbar.show{
    visibility: visible;
    -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
    animation: fadein 0.5s, fadeout 0.5s 2.5s;
  }

  @-webkit-keyframes fadein {
    from {bottom: 0; opacity: 0;}
    to {bottom: 30px; opacity: 1;}
  }

  @keyframes fadein {
    from {bottom: 0; opacity: 0;}
    to {bottom: 30px; opacity: 1;}
  }

  @-webkit-keyframes fadeout {
    from {bottom: 30px; opacity: 1;}
    to {bottom: 0; opacity: 0;}
  }

  @keyframes fadeout {
    from {bottom: 30px; opacity: 1;}
    to {bottom: 0; opacity: 0;}
  }

/* snack bar */
		"""

		self.code_stack.append(temp_code)

	def generate_go_top(self):
		temp_code = """
/* go top btn */
.go-top{
    background-color: #767d9c;
    position: fixed;
    bottom: 16px;
    right: 32px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    color: #1f1f1f;
    text-decoration: none;
    opacity: 0;
    pointer-events: none;
    transition: all .4s;

}
.go-top.active{
    bottom: 32px;
    pointer-events: auto;
    opacity: 1;
}
/* end go top */"""
		self.code_stack.append(temp_code)
