# Add a series of pictures to a feature

You can add one or more pictures to a feature. Below you find an example how to proceed.

## Creating two tables

We will need two tables. One table where the features are stored
and one with a list of pictures.

*Apiary*

* `id` (UUID)
* `geometry`
* ...

*Apiary_pictures*

* `id`
* `apiary_id` (UUID)
* `path` (TEXT)
* ...

## Relations

Create a relation with:

* `apiary` Referenced layer
* `id` Referenced field
* `apiary_picture` Referencing layer
* `apiary_id` Referencing field
* `strength` Composition

<figure>
    <img src="../../../assets/images/add-1-n-pictures-relations.png" width="600px" alt="Relations"/>
</figure>

## Widgets

*apiary*

Set the default value of the field id to `uuid()`.
There is no need to show it in the form, since it will be filled by QField
and does not contain any human readable information.

<figure>
    <a data-fancybox="gallery" href="../../../assets/images/add-1-n-pictures-widgets_hive.png">
     <img src="../../../assets/images/add-1-n-pictures-widgets_hive.png" width="600px" alt="Widgets"/>
    </a>
</figure>

Set the relation widget to `Many to one relation` and add the relation to the form

<figure>
    <img src="../../../assets/images/add-1-n-pictures-widgets_hive2.png" width="600px" alt="Widgets2"/>
</figure>

*picture*

Set the widget type of the field path to `attachment` and add it to the form

<figure>
    <img src="../../../assets/images/add-1-n-pictures-widgets_picture.png" width="600px" alt="Widget picture"/>
</figure>

## Geotagging

Some mobile devices will require Open Camera to be installed in order to enable geotagging.

To enable geotagging perform the following steps:

1. In QField, go to the settings and make sure "Use native Camera" is activated
2. Install the [Open Camera app](https://play.google.com/store/apps/details?id=net.sourceforge.opencamera&hl=en&gl=US) on your mobile device
3. Within the Open Camera settings, make sure geotagging is enabled
4. Within you mobile device settings, set the default camera app to Open Camera
5. Completed! Open Camera will now be utilized while taking pictures with QField
