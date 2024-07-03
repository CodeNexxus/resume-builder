# Generated from D:/Uni/semester_6/Compiler/proj/resume-builder/grammar/Resume.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ResumeParser import ResumeParser
else:
    from ResumeParser import ResumeParser

# This class defines a complete listener for a parse tree produced by ResumeParser.
class ResumeListener(ParseTreeListener):

    # Enter a parse tree produced by ResumeParser#start.
    def enterStart(self, ctx:ResumeParser.StartContext):
        pass

    # Exit a parse tree produced by ResumeParser#start.
    def exitStart(self, ctx:ResumeParser.StartContext):
        pass


    # Enter a parse tree produced by ResumeParser#resume.
    def enterResume(self, ctx:ResumeParser.ResumeContext):
        pass

    # Exit a parse tree produced by ResumeParser#resume.
    def exitResume(self, ctx:ResumeParser.ResumeContext):
        pass


    # Enter a parse tree produced by ResumeParser#optional_features.
    def enterOptional_features(self, ctx:ResumeParser.Optional_featuresContext):
        pass

    # Exit a parse tree produced by ResumeParser#optional_features.
    def exitOptional_features(self, ctx:ResumeParser.Optional_featuresContext):
        pass


    # Enter a parse tree produced by ResumeParser#go_top.
    def enterGo_top(self, ctx:ResumeParser.Go_topContext):
        pass

    # Exit a parse tree produced by ResumeParser#go_top.
    def exitGo_top(self, ctx:ResumeParser.Go_topContext):
        pass


    # Enter a parse tree produced by ResumeParser#autocopy.
    def enterAutocopy(self, ctx:ResumeParser.AutocopyContext):
        pass

    # Exit a parse tree produced by ResumeParser#autocopy.
    def exitAutocopy(self, ctx:ResumeParser.AutocopyContext):
        pass


    # Enter a parse tree produced by ResumeParser#job_title_effect.
    def enterJob_title_effect(self, ctx:ResumeParser.Job_title_effectContext):
        pass

    # Exit a parse tree produced by ResumeParser#job_title_effect.
    def exitJob_title_effect(self, ctx:ResumeParser.Job_title_effectContext):
        pass


    # Enter a parse tree produced by ResumeParser#collapsable_sections.
    def enterCollapsable_sections(self, ctx:ResumeParser.Collapsable_sectionsContext):
        pass

    # Exit a parse tree produced by ResumeParser#collapsable_sections.
    def exitCollapsable_sections(self, ctx:ResumeParser.Collapsable_sectionsContext):
        pass


    # Enter a parse tree produced by ResumeParser#theme_switching.
    def enterTheme_switching(self, ctx:ResumeParser.Theme_switchingContext):
        pass

    # Exit a parse tree produced by ResumeParser#theme_switching.
    def exitTheme_switching(self, ctx:ResumeParser.Theme_switchingContext):
        pass


    # Enter a parse tree produced by ResumeParser#tooltip.
    def enterTooltip(self, ctx:ResumeParser.TooltipContext):
        pass

    # Exit a parse tree produced by ResumeParser#tooltip.
    def exitTooltip(self, ctx:ResumeParser.TooltipContext):
        pass


    # Enter a parse tree produced by ResumeParser#boolean.
    def enterBoolean(self, ctx:ResumeParser.BooleanContext):
        pass

    # Exit a parse tree produced by ResumeParser#boolean.
    def exitBoolean(self, ctx:ResumeParser.BooleanContext):
        pass


    # Enter a parse tree produced by ResumeParser#base_info.
    def enterBase_info(self, ctx:ResumeParser.Base_infoContext):
        pass

    # Exit a parse tree produced by ResumeParser#base_info.
    def exitBase_info(self, ctx:ResumeParser.Base_infoContext):
        pass


    # Enter a parse tree produced by ResumeParser#additional_info.
    def enterAdditional_info(self, ctx:ResumeParser.Additional_infoContext):
        pass

    # Exit a parse tree produced by ResumeParser#additional_info.
    def exitAdditional_info(self, ctx:ResumeParser.Additional_infoContext):
        pass


    # Enter a parse tree produced by ResumeParser#git_scraper.
    def enterGit_scraper(self, ctx:ResumeParser.Git_scraperContext):
        pass

    # Exit a parse tree produced by ResumeParser#git_scraper.
    def exitGit_scraper(self, ctx:ResumeParser.Git_scraperContext):
        pass


    # Enter a parse tree produced by ResumeParser#personal_info.
    def enterPersonal_info(self, ctx:ResumeParser.Personal_infoContext):
        pass

    # Exit a parse tree produced by ResumeParser#personal_info.
    def exitPersonal_info(self, ctx:ResumeParser.Personal_infoContext):
        pass


    # Enter a parse tree produced by ResumeParser#name.
    def enterName(self, ctx:ResumeParser.NameContext):
        pass

    # Exit a parse tree produced by ResumeParser#name.
    def exitName(self, ctx:ResumeParser.NameContext):
        pass


    # Enter a parse tree produced by ResumeParser#surname.
    def enterSurname(self, ctx:ResumeParser.SurnameContext):
        pass

    # Exit a parse tree produced by ResumeParser#surname.
    def exitSurname(self, ctx:ResumeParser.SurnameContext):
        pass


    # Enter a parse tree produced by ResumeParser#job_title.
    def enterJob_title(self, ctx:ResumeParser.Job_titleContext):
        pass

    # Exit a parse tree produced by ResumeParser#job_title.
    def exitJob_title(self, ctx:ResumeParser.Job_titleContext):
        pass


    # Enter a parse tree produced by ResumeParser#birth.
    def enterBirth(self, ctx:ResumeParser.BirthContext):
        pass

    # Exit a parse tree produced by ResumeParser#birth.
    def exitBirth(self, ctx:ResumeParser.BirthContext):
        pass


    # Enter a parse tree produced by ResumeParser#phone.
    def enterPhone(self, ctx:ResumeParser.PhoneContext):
        pass

    # Exit a parse tree produced by ResumeParser#phone.
    def exitPhone(self, ctx:ResumeParser.PhoneContext):
        pass


    # Enter a parse tree produced by ResumeParser#city.
    def enterCity(self, ctx:ResumeParser.CityContext):
        pass

    # Exit a parse tree produced by ResumeParser#city.
    def exitCity(self, ctx:ResumeParser.CityContext):
        pass


    # Enter a parse tree produced by ResumeParser#gmail.
    def enterGmail(self, ctx:ResumeParser.GmailContext):
        pass

    # Exit a parse tree produced by ResumeParser#gmail.
    def exitGmail(self, ctx:ResumeParser.GmailContext):
        pass


    # Enter a parse tree produced by ResumeParser#summary.
    def enterSummary(self, ctx:ResumeParser.SummaryContext):
        pass

    # Exit a parse tree produced by ResumeParser#summary.
    def exitSummary(self, ctx:ResumeParser.SummaryContext):
        pass


    # Enter a parse tree produced by ResumeParser#value.
    def enterValue(self, ctx:ResumeParser.ValueContext):
        pass

    # Exit a parse tree produced by ResumeParser#value.
    def exitValue(self, ctx:ResumeParser.ValueContext):
        pass


    # Enter a parse tree produced by ResumeParser#skills.
    def enterSkills(self, ctx:ResumeParser.SkillsContext):
        pass

    # Exit a parse tree produced by ResumeParser#skills.
    def exitSkills(self, ctx:ResumeParser.SkillsContext):
        pass


    # Enter a parse tree produced by ResumeParser#jobinja_scraper.
    def enterJobinja_scraper(self, ctx:ResumeParser.Jobinja_scraperContext):
        pass

    # Exit a parse tree produced by ResumeParser#jobinja_scraper.
    def exitJobinja_scraper(self, ctx:ResumeParser.Jobinja_scraperContext):
        pass


    # Enter a parse tree produced by ResumeParser#hard_skills.
    def enterHard_skills(self, ctx:ResumeParser.Hard_skillsContext):
        pass

    # Exit a parse tree produced by ResumeParser#hard_skills.
    def exitHard_skills(self, ctx:ResumeParser.Hard_skillsContext):
        pass


    # Enter a parse tree produced by ResumeParser#hard_skill.
    def enterHard_skill(self, ctx:ResumeParser.Hard_skillContext):
        pass

    # Exit a parse tree produced by ResumeParser#hard_skill.
    def exitHard_skill(self, ctx:ResumeParser.Hard_skillContext):
        pass


    # Enter a parse tree produced by ResumeParser#hard_skill_name.
    def enterHard_skill_name(self, ctx:ResumeParser.Hard_skill_nameContext):
        pass

    # Exit a parse tree produced by ResumeParser#hard_skill_name.
    def exitHard_skill_name(self, ctx:ResumeParser.Hard_skill_nameContext):
        pass


    # Enter a parse tree produced by ResumeParser#rate.
    def enterRate(self, ctx:ResumeParser.RateContext):
        pass

    # Exit a parse tree produced by ResumeParser#rate.
    def exitRate(self, ctx:ResumeParser.RateContext):
        pass


    # Enter a parse tree produced by ResumeParser#soft_skills.
    def enterSoft_skills(self, ctx:ResumeParser.Soft_skillsContext):
        pass

    # Exit a parse tree produced by ResumeParser#soft_skills.
    def exitSoft_skills(self, ctx:ResumeParser.Soft_skillsContext):
        pass


    # Enter a parse tree produced by ResumeParser#soft_skill.
    def enterSoft_skill(self, ctx:ResumeParser.Soft_skillContext):
        pass

    # Exit a parse tree produced by ResumeParser#soft_skill.
    def exitSoft_skill(self, ctx:ResumeParser.Soft_skillContext):
        pass


    # Enter a parse tree produced by ResumeParser#soft_skill_name.
    def enterSoft_skill_name(self, ctx:ResumeParser.Soft_skill_nameContext):
        pass

    # Exit a parse tree produced by ResumeParser#soft_skill_name.
    def exitSoft_skill_name(self, ctx:ResumeParser.Soft_skill_nameContext):
        pass


    # Enter a parse tree produced by ResumeParser#languages.
    def enterLanguages(self, ctx:ResumeParser.LanguagesContext):
        pass

    # Exit a parse tree produced by ResumeParser#languages.
    def exitLanguages(self, ctx:ResumeParser.LanguagesContext):
        pass


    # Enter a parse tree produced by ResumeParser#language.
    def enterLanguage(self, ctx:ResumeParser.LanguageContext):
        pass

    # Exit a parse tree produced by ResumeParser#language.
    def exitLanguage(self, ctx:ResumeParser.LanguageContext):
        pass


    # Enter a parse tree produced by ResumeParser#language_name.
    def enterLanguage_name(self, ctx:ResumeParser.Language_nameContext):
        pass

    # Exit a parse tree produced by ResumeParser#language_name.
    def exitLanguage_name(self, ctx:ResumeParser.Language_nameContext):
        pass


    # Enter a parse tree produced by ResumeParser#certificates.
    def enterCertificates(self, ctx:ResumeParser.CertificatesContext):
        pass

    # Exit a parse tree produced by ResumeParser#certificates.
    def exitCertificates(self, ctx:ResumeParser.CertificatesContext):
        pass


    # Enter a parse tree produced by ResumeParser#certificate.
    def enterCertificate(self, ctx:ResumeParser.CertificateContext):
        pass

    # Exit a parse tree produced by ResumeParser#certificate.
    def exitCertificate(self, ctx:ResumeParser.CertificateContext):
        pass


    # Enter a parse tree produced by ResumeParser#link.
    def enterLink(self, ctx:ResumeParser.LinkContext):
        pass

    # Exit a parse tree produced by ResumeParser#link.
    def exitLink(self, ctx:ResumeParser.LinkContext):
        pass


    # Enter a parse tree produced by ResumeParser#institution.
    def enterInstitution(self, ctx:ResumeParser.InstitutionContext):
        pass

    # Exit a parse tree produced by ResumeParser#institution.
    def exitInstitution(self, ctx:ResumeParser.InstitutionContext):
        pass


    # Enter a parse tree produced by ResumeParser#socials.
    def enterSocials(self, ctx:ResumeParser.SocialsContext):
        pass

    # Exit a parse tree produced by ResumeParser#socials.
    def exitSocials(self, ctx:ResumeParser.SocialsContext):
        pass


    # Enter a parse tree produced by ResumeParser#social.
    def enterSocial(self, ctx:ResumeParser.SocialContext):
        pass

    # Exit a parse tree produced by ResumeParser#social.
    def exitSocial(self, ctx:ResumeParser.SocialContext):
        pass


    # Enter a parse tree produced by ResumeParser#social_name.
    def enterSocial_name(self, ctx:ResumeParser.Social_nameContext):
        pass

    # Exit a parse tree produced by ResumeParser#social_name.
    def exitSocial_name(self, ctx:ResumeParser.Social_nameContext):
        pass


    # Enter a parse tree produced by ResumeParser#projects.
    def enterProjects(self, ctx:ResumeParser.ProjectsContext):
        pass

    # Exit a parse tree produced by ResumeParser#projects.
    def exitProjects(self, ctx:ResumeParser.ProjectsContext):
        pass


    # Enter a parse tree produced by ResumeParser#project.
    def enterProject(self, ctx:ResumeParser.ProjectContext):
        pass

    # Exit a parse tree produced by ResumeParser#project.
    def exitProject(self, ctx:ResumeParser.ProjectContext):
        pass


    # Enter a parse tree produced by ResumeParser#project_title.
    def enterProject_title(self, ctx:ResumeParser.Project_titleContext):
        pass

    # Exit a parse tree produced by ResumeParser#project_title.
    def exitProject_title(self, ctx:ResumeParser.Project_titleContext):
        pass


    # Enter a parse tree produced by ResumeParser#project_description.
    def enterProject_description(self, ctx:ResumeParser.Project_descriptionContext):
        pass

    # Exit a parse tree produced by ResumeParser#project_description.
    def exitProject_description(self, ctx:ResumeParser.Project_descriptionContext):
        pass


    # Enter a parse tree produced by ResumeParser#project_url.
    def enterProject_url(self, ctx:ResumeParser.Project_urlContext):
        pass

    # Exit a parse tree produced by ResumeParser#project_url.
    def exitProject_url(self, ctx:ResumeParser.Project_urlContext):
        pass


    # Enter a parse tree produced by ResumeParser#work_experience.
    def enterWork_experience(self, ctx:ResumeParser.Work_experienceContext):
        pass

    # Exit a parse tree produced by ResumeParser#work_experience.
    def exitWork_experience(self, ctx:ResumeParser.Work_experienceContext):
        pass


    # Enter a parse tree produced by ResumeParser#job.
    def enterJob(self, ctx:ResumeParser.JobContext):
        pass

    # Exit a parse tree produced by ResumeParser#job.
    def exitJob(self, ctx:ResumeParser.JobContext):
        pass


    # Enter a parse tree produced by ResumeParser#responsibility_list.
    def enterResponsibility_list(self, ctx:ResumeParser.Responsibility_listContext):
        pass

    # Exit a parse tree produced by ResumeParser#responsibility_list.
    def exitResponsibility_list(self, ctx:ResumeParser.Responsibility_listContext):
        pass


    # Enter a parse tree produced by ResumeParser#responsibility.
    def enterResponsibility(self, ctx:ResumeParser.ResponsibilityContext):
        pass

    # Exit a parse tree produced by ResumeParser#responsibility.
    def exitResponsibility(self, ctx:ResumeParser.ResponsibilityContext):
        pass


    # Enter a parse tree produced by ResumeParser#company.
    def enterCompany(self, ctx:ResumeParser.CompanyContext):
        pass

    # Exit a parse tree produced by ResumeParser#company.
    def exitCompany(self, ctx:ResumeParser.CompanyContext):
        pass


    # Enter a parse tree produced by ResumeParser#position.
    def enterPosition(self, ctx:ResumeParser.PositionContext):
        pass

    # Exit a parse tree produced by ResumeParser#position.
    def exitPosition(self, ctx:ResumeParser.PositionContext):
        pass


    # Enter a parse tree produced by ResumeParser#educations.
    def enterEducations(self, ctx:ResumeParser.EducationsContext):
        pass

    # Exit a parse tree produced by ResumeParser#educations.
    def exitEducations(self, ctx:ResumeParser.EducationsContext):
        pass


    # Enter a parse tree produced by ResumeParser#education.
    def enterEducation(self, ctx:ResumeParser.EducationContext):
        pass

    # Exit a parse tree produced by ResumeParser#education.
    def exitEducation(self, ctx:ResumeParser.EducationContext):
        pass


    # Enter a parse tree produced by ResumeParser#degree.
    def enterDegree(self, ctx:ResumeParser.DegreeContext):
        pass

    # Exit a parse tree produced by ResumeParser#degree.
    def exitDegree(self, ctx:ResumeParser.DegreeContext):
        pass


    # Enter a parse tree produced by ResumeParser#start_date.
    def enterStart_date(self, ctx:ResumeParser.Start_dateContext):
        pass

    # Exit a parse tree produced by ResumeParser#start_date.
    def exitStart_date(self, ctx:ResumeParser.Start_dateContext):
        pass


    # Enter a parse tree produced by ResumeParser#end_date.
    def enterEnd_date(self, ctx:ResumeParser.End_dateContext):
        pass

    # Exit a parse tree produced by ResumeParser#end_date.
    def exitEnd_date(self, ctx:ResumeParser.End_dateContext):
        pass



del ResumeParser