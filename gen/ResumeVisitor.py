# Generated from C:/Users/DarknesS/source/repos/dsl/grammar/Resume.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ResumeParser import ResumeParser
else:
    from ResumeParser import ResumeParser

# This class defines a complete generic visitor for a parse tree produced by ResumeParser.

class ResumeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ResumeParser#start.
    def visitStart(self, ctx:ResumeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#resume.
    def visitResume(self, ctx:ResumeParser.ResumeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#optional_features.
    def visitOptional_features(self, ctx:ResumeParser.Optional_featuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#go_top.
    def visitGo_top(self, ctx:ResumeParser.Go_topContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#autocopy.
    def visitAutocopy(self, ctx:ResumeParser.AutocopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#job_title_effect.
    def visitJob_title_effect(self, ctx:ResumeParser.Job_title_effectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#interactive_skill_bars.
    def visitInteractive_skill_bars(self, ctx:ResumeParser.Interactive_skill_barsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#collapsable_sections.
    def visitCollapsable_sections(self, ctx:ResumeParser.Collapsable_sectionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#dynamic_theme.
    def visitDynamic_theme(self, ctx:ResumeParser.Dynamic_themeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#switching.
    def visitSwitching(self, ctx:ResumeParser.SwitchingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#tooltip.
    def visitTooltip(self, ctx:ResumeParser.TooltipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#pdf_output.
    def visitPdf_output(self, ctx:ResumeParser.Pdf_outputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#boolean.
    def visitBoolean(self, ctx:ResumeParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#base_info.
    def visitBase_info(self, ctx:ResumeParser.Base_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#additional_info.
    def visitAdditional_info(self, ctx:ResumeParser.Additional_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#git_scraper.
    def visitGit_scraper(self, ctx:ResumeParser.Git_scraperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#personal_info.
    def visitPersonal_info(self, ctx:ResumeParser.Personal_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#name.
    def visitName(self, ctx:ResumeParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#surname.
    def visitSurname(self, ctx:ResumeParser.SurnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#job_title.
    def visitJob_title(self, ctx:ResumeParser.Job_titleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#birth.
    def visitBirth(self, ctx:ResumeParser.BirthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#phone.
    def visitPhone(self, ctx:ResumeParser.PhoneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#city.
    def visitCity(self, ctx:ResumeParser.CityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#gmail.
    def visitGmail(self, ctx:ResumeParser.GmailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#summary.
    def visitSummary(self, ctx:ResumeParser.SummaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#value.
    def visitValue(self, ctx:ResumeParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#skills.
    def visitSkills(self, ctx:ResumeParser.SkillsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#jobinja_scraper.
    def visitJobinja_scraper(self, ctx:ResumeParser.Jobinja_scraperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#hard_skills.
    def visitHard_skills(self, ctx:ResumeParser.Hard_skillsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#hard_skill.
    def visitHard_skill(self, ctx:ResumeParser.Hard_skillContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#hard_skill_name.
    def visitHard_skill_name(self, ctx:ResumeParser.Hard_skill_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#rate.
    def visitRate(self, ctx:ResumeParser.RateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#soft_skills.
    def visitSoft_skills(self, ctx:ResumeParser.Soft_skillsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#soft_skill.
    def visitSoft_skill(self, ctx:ResumeParser.Soft_skillContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#soft_skill_name.
    def visitSoft_skill_name(self, ctx:ResumeParser.Soft_skill_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#languages.
    def visitLanguages(self, ctx:ResumeParser.LanguagesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#language.
    def visitLanguage(self, ctx:ResumeParser.LanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#language_name.
    def visitLanguage_name(self, ctx:ResumeParser.Language_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#certificates.
    def visitCertificates(self, ctx:ResumeParser.CertificatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#certificate.
    def visitCertificate(self, ctx:ResumeParser.CertificateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#link.
    def visitLink(self, ctx:ResumeParser.LinkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#institution.
    def visitInstitution(self, ctx:ResumeParser.InstitutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#socials.
    def visitSocials(self, ctx:ResumeParser.SocialsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#social.
    def visitSocial(self, ctx:ResumeParser.SocialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#social_name.
    def visitSocial_name(self, ctx:ResumeParser.Social_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#projects.
    def visitProjects(self, ctx:ResumeParser.ProjectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#project.
    def visitProject(self, ctx:ResumeParser.ProjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#project_title.
    def visitProject_title(self, ctx:ResumeParser.Project_titleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#project_description.
    def visitProject_description(self, ctx:ResumeParser.Project_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#project_url.
    def visitProject_url(self, ctx:ResumeParser.Project_urlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#work_experience.
    def visitWork_experience(self, ctx:ResumeParser.Work_experienceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#job.
    def visitJob(self, ctx:ResumeParser.JobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#responsibility_list.
    def visitResponsibility_list(self, ctx:ResumeParser.Responsibility_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#responsibility.
    def visitResponsibility(self, ctx:ResumeParser.ResponsibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#company.
    def visitCompany(self, ctx:ResumeParser.CompanyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#position.
    def visitPosition(self, ctx:ResumeParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#educations.
    def visitEducations(self, ctx:ResumeParser.EducationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#education.
    def visitEducation(self, ctx:ResumeParser.EducationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#degree.
    def visitDegree(self, ctx:ResumeParser.DegreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#start_date.
    def visitStart_date(self, ctx:ResumeParser.Start_dateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#end_date.
    def visitEnd_date(self, ctx:ResumeParser.End_dateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#optional_features.
    def visitOptional_features(self, ctx:ResumeParser.Optional_featuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#theme_switch.
    def visitTheme_switch(self, ctx:ResumeParser.Theme_switchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#pdf_download.
    def visitPdf_download(self, ctx:ResumeParser.Pdf_downloadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#section_mod.
    def visitSection_mod(self, ctx:ResumeParser.Section_modContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#collapsable.
    def visitCollapsable(self, ctx:ResumeParser.CollapsableContext):
        return self.visitChildren(ctx)



del ResumeParser