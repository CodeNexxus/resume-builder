# Generated from C:/Users/pars/Desktop/code nuxxus/grammar/Resume.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ResumeParser#skills.
    def enterSkills(self, ctx:ResumeParser.SkillsContext):
        pass

    # Exit a parse tree produced by ResumeParser#skills.
    def exitSkills(self, ctx:ResumeParser.SkillsContext):
        pass


    # Enter a parse tree produced by ResumeParser#hard_skills.
    def enterHard_skills(self, ctx:ResumeParser.Hard_skillsContext):
        pass

    # Exit a parse tree produced by ResumeParser#hard_skills.
    def exitHard_skills(self, ctx:ResumeParser.Hard_skillsContext):
        pass


    # Enter a parse tree produced by ResumeParser#hard_skill_list.
    def enterHard_skill_list(self, ctx:ResumeParser.Hard_skill_listContext):
        pass

    # Exit a parse tree produced by ResumeParser#hard_skill_list.
    def exitHard_skill_list(self, ctx:ResumeParser.Hard_skill_listContext):
        pass


    # Enter a parse tree produced by ResumeParser#hard_skill.
    def enterHard_skill(self, ctx:ResumeParser.Hard_skillContext):
        pass

    # Exit a parse tree produced by ResumeParser#hard_skill.
    def exitHard_skill(self, ctx:ResumeParser.Hard_skillContext):
        pass


    # Enter a parse tree produced by ResumeParser#soft_skills.
    def enterSoft_skills(self, ctx:ResumeParser.Soft_skillsContext):
        pass

    # Exit a parse tree produced by ResumeParser#soft_skills.
    def exitSoft_skills(self, ctx:ResumeParser.Soft_skillsContext):
        pass


    # Enter a parse tree produced by ResumeParser#soft_skill_list.
    def enterSoft_skill_list(self, ctx:ResumeParser.Soft_skill_listContext):
        pass

    # Exit a parse tree produced by ResumeParser#soft_skill_list.
    def exitSoft_skill_list(self, ctx:ResumeParser.Soft_skill_listContext):
        pass


    # Enter a parse tree produced by ResumeParser#soft_skill.
    def enterSoft_skill(self, ctx:ResumeParser.Soft_skillContext):
        pass

    # Exit a parse tree produced by ResumeParser#soft_skill.
    def exitSoft_skill(self, ctx:ResumeParser.Soft_skillContext):
        pass


    # Enter a parse tree produced by ResumeParser#languages.
    def enterLanguages(self, ctx:ResumeParser.LanguagesContext):
        pass

    # Exit a parse tree produced by ResumeParser#languages.
    def exitLanguages(self, ctx:ResumeParser.LanguagesContext):
        pass


    # Enter a parse tree produced by ResumeParser#language_list.
    def enterLanguage_list(self, ctx:ResumeParser.Language_listContext):
        pass

    # Exit a parse tree produced by ResumeParser#language_list.
    def exitLanguage_list(self, ctx:ResumeParser.Language_listContext):
        pass


    # Enter a parse tree produced by ResumeParser#language.
    def enterLanguage(self, ctx:ResumeParser.LanguageContext):
        pass

    # Exit a parse tree produced by ResumeParser#language.
    def exitLanguage(self, ctx:ResumeParser.LanguageContext):
        pass


    # Enter a parse tree produced by ResumeParser#certificates.
    def enterCertificates(self, ctx:ResumeParser.CertificatesContext):
        pass

    # Exit a parse tree produced by ResumeParser#certificates.
    def exitCertificates(self, ctx:ResumeParser.CertificatesContext):
        pass


    # Enter a parse tree produced by ResumeParser#certificate_list.
    def enterCertificate_list(self, ctx:ResumeParser.Certificate_listContext):
        pass

    # Exit a parse tree produced by ResumeParser#certificate_list.
    def exitCertificate_list(self, ctx:ResumeParser.Certificate_listContext):
        pass


    # Enter a parse tree produced by ResumeParser#certificate.
    def enterCertificate(self, ctx:ResumeParser.CertificateContext):
        pass

    # Exit a parse tree produced by ResumeParser#certificate.
    def exitCertificate(self, ctx:ResumeParser.CertificateContext):
        pass


    # Enter a parse tree produced by ResumeParser#socials.
    def enterSocials(self, ctx:ResumeParser.SocialsContext):
        pass

    # Exit a parse tree produced by ResumeParser#socials.
    def exitSocials(self, ctx:ResumeParser.SocialsContext):
        pass


    # Enter a parse tree produced by ResumeParser#social_list.
    def enterSocial_list(self, ctx:ResumeParser.Social_listContext):
        pass

    # Exit a parse tree produced by ResumeParser#social_list.
    def exitSocial_list(self, ctx:ResumeParser.Social_listContext):
        pass


    # Enter a parse tree produced by ResumeParser#social.
    def enterSocial(self, ctx:ResumeParser.SocialContext):
        pass

    # Exit a parse tree produced by ResumeParser#social.
    def exitSocial(self, ctx:ResumeParser.SocialContext):
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



del ResumeParser