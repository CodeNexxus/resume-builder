# Generated from D:/Uni/semester_6/Compiler/project/resume-builder/grammar/Resume.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by ResumeParser#institution.
    def visitInstitution(self, ctx:ResumeParser.InstitutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#url.
    def visitUrl(self, ctx:ResumeParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#socials.
    def visitSocials(self, ctx:ResumeParser.SocialsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#social_list.
    def visitSocial_list(self, ctx:ResumeParser.Social_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#social.
    def visitSocial(self, ctx:ResumeParser.SocialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#projects.
    def visitProjects(self, ctx:ResumeParser.ProjectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#project.
    def visitProject(self, ctx:ResumeParser.ProjectContext):
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


    # Visit a parse tree produced by ResumeParser#educations.
    def visitEducations(self, ctx:ResumeParser.EducationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResumeParser#education.
    def visitEducation(self, ctx:ResumeParser.EducationContext):
        return self.visitChildren(ctx)



del ResumeParser