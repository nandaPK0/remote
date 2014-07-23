#from os.path import join

from django.contrib.auth.models import User 
from django.db import models

from .tasks import project_created 
#from pearl.settings import BASE_DIR 


FASTQ_EXTENSION = ".fastq"
FASTQC_TAIL = "_fastqc/"
REPORT_DIR = "files/Report/"
REPORT_NAME = "fastqc_report.html"
FIRST = 0
LAST = -1

TISSUE_CHOICES = (
    ('Tissue_A', 'TISSUE_A'),
    ('Tissue_B', 'TISSUE_B'),
)
DISEASE_CHOICES = (
    ('Disease A', 'Disease A'),
    ('Disease B', 'Disease B'),
)

UPLOADING_FILES = 0
QUALITY_CONTROL = 1
START_PROCESSING = 2
DO_PROCESSING = 3
FINAL_REPORT = 4


STATUS_OPTIONS = (
    (UPLOADING_FILES, 'Uploading Files.'),
    (QUALITY_CONTROL, 'Checking Quality.'),
    (START_PROCESSING, 'Review Quality.'),
    (DO_PROCESSING, 'Processing the file.'),
    (FINAL_REPORT, 'Report Generated.')
)

class NewProject(models.Model):
    customer = models.ForeignKey(User, related_name='original_customer_id')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    file_type = models.CharField(max_length=10)
    vcf_file1 = models.URLField(max_length=200, blank=True)
    total_fastq_files = models.SmallIntegerField(default=0, 
                                                 blank=True, 
                                                 null=True,)
    fastq_file1 = models.URLField(max_length=200, blank=True)
    fastq_file2 = models.URLField(max_length=200, blank=True)
    file_list = models.CharField(max_length=200, blank=True)
    paired_end_distance = models.IntegerField(blank=True, null=True)
    tissue = models.CharField(max_length=30, default='',
            choices=TISSUE_CHOICES,)
    disease = models.CharField(max_length=100, default='',
            choices=DISEASE_CHOICES,)
    status = models.IntegerField(choices=STATUS_OPTIONS, default=UPLOADING_FILES)
    start_pocessing = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
        #return "{} : {}".format(self.customer.username, self.name)

    class Meta:
        ordering = ['updated_at']
        permissions = (
            ('view_report', 'view_report'),
        )

    def save(self, *args, **kwargs):
        super(NewProject, self).save(*args, **kwargs)
        project_created.apply_async(args=[self.pk,])

    def qc_report_links(self):
        url_list = self.url_list()
        links = []
        for url in url_list:
            """
            file_name = url.split('/')[LAST]
            file_name_root = file_name.split(FASTQ_EXTENSION)[FIRST]
            dir_name = file_name_root + FASTQC_TAIL 
            report_link = join(BASE_DIR, REPORT_DIR, str(self.pk), dir_name, REPORT_NAME)
            links.append(report_link)
            """
            file_name = url.split('/')[LAST]
            file_name_root = file_name.split(FASTQ_EXTENSION)[FIRST]
            dir_name = file_name_root + FASTQC_TAIL 
            links.append(dir_name)
        return links 

    def url_list(self):
        url_list = [self.fastq_file1, self.fastq_file2, self.vcf_file1]
        return filter(None, url_list)


class ProjectReport(models.Model):
    project = models.ForeignKey(NewProject, related_name='project_as_foreign_key')
    pdf_file = models.CharField(max_length=100, default='')
    data = models.CharField(max_length=20, default='')

    def __unicode__(self):
        return self.project.name 


