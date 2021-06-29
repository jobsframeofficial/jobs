# Generated by Django 3.2.4 on 2021-06-29 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categary_label',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('choice_id', models.CharField(max_length=100)),
                ('choice_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courses_and_certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_name', models.CharField(max_length=200)),
                ('organised_by', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=50000)),
                ('post_date', models.DateField()),
                ('last_date', models.DateField()),
                ('apply_link', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('looking_for', models.CharField(max_length=1500)),
                ('profile_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=50000)),
                ('location', models.CharField(max_length=200)),
                ('exp_from', models.IntegerField()),
                ('exp_to', models.IntegerField()),
                ('post_date', models.DateField()),
                ('last_date', models.DateField()),
                ('apply_link', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('mac_address', models.CharField(default='1', max_length=200)),
                ('index_page', models.IntegerField(default=0)),
                ('detail_page', models.IntegerField(default=0)),
                ('contact_us', models.IntegerField(default=0)),
                ('about_us', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Catagories',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('catagory', models.CharField(choices=[('all_jobs', 'All Jobs'), ('private_tech_jobs', 'Private Tech Jobs'), ('private_non_tech_jobs', 'Private Non Tech Jobs'), ('part_time_jobs', 'Part Time Jobs'), ('govt_tech_jobs', 'Govt. Tech Jobs'), ('govt_non_tech_jobs', 'Govt. Non Tech Jobs'), ('internships', 'Internships'), ('competative_coding', 'Competative Coding'), ('free_courses', 'Free Courses'), ('certifications', 'Certifications')], default=1, max_length=100)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs1.job')),
            ],
            options={
                'unique_together': {('job_id', 'catagory')},
            },
        ),
    ]
