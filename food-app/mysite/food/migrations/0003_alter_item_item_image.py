# Generated by Django 5.2.4 on 2025-07-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.bing.com/images/search?view=detailV2&ccid=kSEb4dgL&id=1CCD935EA9C6BB3F18080B4E053816AFACBBB9AF&thid=OIP.kSEb4dgLYwPHCj0QKdVcvQHaHk&mediaurl=https%3a%2f%2ftoppng.com%2fuploads%2fpreview%2fclipart-free-seaweed-clipart-draw-food-placeholder-11562968708qhzooxrjly.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.91211be1d80b6303c70a3d1029d55cbd%3frik%3dr7m7rK8WOAVOCw%26pid%3dImgRaw%26r%3d0&exph=859&expw=840&q=placeholder+food+image&simid=607997547233891759&FORM=IRPRST&ck=C1A8ACFD486373E13EFBED010FCB9548&selectedIndex=0&itb=0&idpp=overlayview&ajaxhist=0&ajaxserp=0', max_length=500),
        ),
    ]
