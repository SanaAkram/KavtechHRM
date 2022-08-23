# Generated by Django 4.0.3 on 2022-08-22 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0006_userprofile_job_openings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('difficulty_level', models.IntegerField(choices=[(0, 'Fresher'), (1, 'Intermediate'), (2, 'Advanced'), (3, 'Expert')], default=0, verbose_name='Difficulty level')),
                ('opt_1', models.CharField(max_length=255, verbose_name='Option 1')),
                ('opt_2', models.CharField(max_length=255, verbose_name='Option 2')),
                ('opt_3', models.CharField(max_length=255, verbose_name='Option 3')),
                ('opt_4', models.CharField(max_length=255, verbose_name='Option 4')),
                ('right_opt', models.CharField(max_length=100, verbose_name='Right option')),
                ('score', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserSubmittedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_ans', models.CharField(max_length=255)),
                ('score', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Quiz', max_length=255, verbose_name='Quiz Title')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.category')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='quiz.quizzes'),
        ),
    ]
