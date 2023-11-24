1. IMPORT GEEMAP & OTHER LIB
2. AUTOMATE IMPORT FILE FROM COPERNICUS
3. DO AC IF L1C
4. IF NOT CAN DO CALIBRATION RIGHT AWAY

```python
# Modules
import geemap
import ee
import numpy
import matplotlib.pyplot as plt
import folium
import IPython.display as disp
```


```python
# Authenticate Earth Engine
ee.Authenticate()
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<p>To authorize access needed by Earth Engine, open the following
        URL in a web browser and follow the instructions:</p>
        <p><a href=https://code.earthengine.google.com/client-auth?scopes=https%3A//www.googleapis.com/auth/earthengine%20https%3A//www.googleapis.com/auth/devstorage.full_control&request_id=gQqj_RFxscBJi4C3E-XxgU7rkqMvB0z3ciiEYUKSAlI&tc=VlIcPOh8AMJe4DksvkqSKC2GIZ7X_MNn1NDsP57Ahc4&cc=WPlQkNUxh4oewawEPT3ksrSE6uaqP0gRPKjRyZwMyFg>https://code.earthengine.google.com/client-auth?scopes=https%3A//www.googleapis.com/auth/earthengine%20https%3A//www.googleapis.com/auth/devstorage.full_control&request_id=gQqj_RFxscBJi4C3E-XxgU7rkqMvB0z3ciiEYUKSAlI&tc=VlIcPOh8AMJe4DksvkqSKC2GIZ7X_MNn1NDsP57Ahc4&cc=WPlQkNUxh4oewawEPT3ksrSE6uaqP0gRPKjRyZwMyFg</a></p>
        <p>The authorization workflow will generate a code, which you should paste in the box below.</p>



    Enter verification code:  4/1AfJohXmW3QeRLSSueXyV0bf9pD9EMsS1rZU4lY95kcdbSl1HkGGQxmMUH0w
    

    
    Successfully saved authorization token.
    


```python
# Initiate the library
ee.Initialize()
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Define a method for displaying Earth Engine image tiles to folium map.
def add_ee_layer(self, ee_image_object, vis_params, name):
  map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
  folium.raster_layers.TileLayer(
    tiles = map_id_dict['tile_fetcher'].url_format,
    attr = 'Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
    name = name,
    overlay = True,
    control = True
  ).add_to(self)

# Add EE drawing method to folium.
folium.Map.add_ee_layer = add_ee_layer
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
Sentinel_trial = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
Region = ee.Geometry.Rectangle(130.9825040586519,-12.591236530819916, 130.80603616314409,-12.482652274143653)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
Dataset_db = ee.Image(ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                       .filterBounds(Region)
                       .filterDate(ee.Date('2023-09-01'), ee.Date('2023-09-02'))
                       .first()
                       .clip(Region))
Dataset_fl = ee.Image(ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                       .filterBounds(Region)
                       .filterDate(ee.Date('2023-09-01'), ee.Date('2023-09-02'))
                       .first()
                       .clip(Region))
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
Dataset_db.bandNames().getInfo()
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>






    ['B1',
     'B2',
     'B3',
     'B4',
     'B5',
     'B6',
     'B7',
     'B8',
     'B8A',
     'B9',
     'B11',
     'B12',
     'AOT',
     'WVP',
     'SCL',
     'TCI_R',
     'TCI_G',
     'TCI_B',
     'MSK_CLDPRB',
     'MSK_SNWPRB',
     'QA10',
     'QA20',
     'QA60']




```python
url = Dataset_db.select('B11').getThumbURL({'min': -20, 'max': 0})
disp.Image(url=url, width=800)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>






<img src="https://earthengine.googleapis.com/v1/projects/earthengine-legacy/thumbnails/bf54b1b601e05ae1f6401d4fde307699-c1c8f880956430eb424ef1161c362ea8:getPixels" width="800"/>




```python
location = Region.centroid().coordinates().getInfo()[::-1]

# Make an RGB color composite image (VV,VH,VV/VH).
rgb = ee.Image.rgb(Dataset_db.select('B12'),
                   Dataset_db.select('B11'),
                   Dataset_db.select('B11').divide(Dataset_db.select('B12')))

# Create the map object.
m = folium.Map(location=location, zoom_start=13)

# Add the S1 rgb composite to the map object.
m.add_ee_layer(rgb, {'min': [-20, -20, 0], 'max': [0, 0, 2]}, 'FFA')

# Add a layer control panel to the map.
m.add_child(folium.LayerControl())

# Display the map.
display(m)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.7.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_aabb384a41779ccb0b71a59de832e167 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_aabb384a41779ccb0b71a59de832e167&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_aabb384a41779ccb0b71a59de832e167 = L.map(
                &quot;map_aabb384a41779ccb0b71a59de832e167&quot;,
                {
                    center: [-12.536954984912139, 130.89427011089856],
                    crs: L.CRS.EPSG3857,
                    zoom: 13,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_8a6464a2dc2d9ee35dafb704211dbc66 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_8a6464a2dc2d9ee35dafb704211dbc66.addTo(map_aabb384a41779ccb0b71a59de832e167);

            var tile_layer_e027d168a826a3d26bd92eaf1aa1e8e0 = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/b0f9a3d42c265b40d6517a3927d12599-ac6dd325b5c7d379b8bbb9723b15b198/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_e027d168a826a3d26bd92eaf1aa1e8e0.addTo(map_aabb384a41779ccb0b71a59de832e167);

            var layer_control_b623127d3f723d5bf1f4774ea3b60e88_layers = {
                base_layers : {
                    &quot;openstreetmap&quot; : tile_layer_8a6464a2dc2d9ee35dafb704211dbc66,
                },
                overlays :  {
                    &quot;FFA&quot; : tile_layer_e027d168a826a3d26bd92eaf1aa1e8e0,
                },
            };
            let layer_control_b623127d3f723d5bf1f4774ea3b60e88 = L.control.layers(
                layer_control_b623127d3f723d5bf1f4774ea3b60e88_layers.base_layers,
                layer_control_b623127d3f723d5bf1f4774ea3b60e88_layers.overlays,
                {&quot;autoZIndex&quot;: true, &quot;collapsed&quot;: true, &quot;position&quot;: &quot;topright&quot;}
            ).addTo(map_aabb384a41779ccb0b71a59de832e167);


&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>


# **Cloud Masking**


```python
# Date Validate
Start_Date = '2023-09-01'
End_Date = '2023-09-02'
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Cloud masking
CLOUD_FILTER = 60
CLD_PRB_THRESH = 50
NIR_DRK_THRESH = 0.15
CLD_PRJ_DIST = 1
BUFFER = 50
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
def Get_S2_SR_Cloud_Col(Region, start_date, end_date):
    # Import and filter S2 SR.
    S2_SR = (ee.ImageCollection('COPERNICUS/S2_SR')
        .filterBounds(Region)
        .filterDate(Start_Date, End_Date)
        .filter(ee.Filter.lte('CLOUDY_PIXEL_PERCENTAGE', CLOUD_FILTER)))

    # Import and filter s2cloudless.
    S2_Cloudless = (ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')
        .filterBounds(Region)
        .filterDate(Start_Date, End_Date))

    # Join the filtered s2cloudless collection to the SR collection by the 'system:index' property.
    return ee.ImageCollection(ee.Join.saveFirst('s2cloudless').apply(**{
        'primary': S2_SR,
        'secondary': S2_Cloudless,
        'condition': ee.Filter.equals(**{
            'leftField': 'system:index',
            'rightField': 'system:index'
        })
    }))
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
S2_SR_Cloud_Col_Eval = Get_S2_SR_Cloud_Col(Region, Start_Date, End_Date)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
def add_cloud_bands(img):
    # Get s2cloudless image, subset the probability band.
    cld_prb = ee.Image(img.get('s2cloudless')).select('probability')

    # Condition s2cloudless by the probability threshold value.
    is_cloud = cld_prb.gt(CLD_PRB_THRESH).rename('clouds')

    # Add the cloud probability layer and cloud mask as image bands.
    return img.addBands(ee.Image([cld_prb, is_cloud]))
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
def add_shadow_bands(img):
    # Identify water pixels from the SCL band.
    not_water = img.select('SCL').neq(6)

    # Identify dark NIR pixels that are not water (potential cloud shadow pixels).
    SR_BAND_SCALE = 1e4
    dark_pixels = img.select('B8').lt(NIR_DRK_THRESH*SR_BAND_SCALE).multiply(not_water).rename('dark_pixels')

    # Determine the direction to project cloud shadow from clouds (assumes UTM projection).
    shadow_azimuth = ee.Number(90).subtract(ee.Number(img.get('MEAN_SOLAR_AZIMUTH_ANGLE')));

    # Project shadows from clouds for the distance specified by the CLD_PRJ_DIST input.
    cld_proj = (img.select('clouds').directionalDistanceTransform(shadow_azimuth, CLD_PRJ_DIST*10)
        .reproject(**{'crs': img.select(0).projection(), 'scale': 100})
        .select('distance')
        .mask()
        .rename('cloud_transform'))

    # Identify the intersection of dark pixels with cloud shadow projection.
    shadows = cld_proj.multiply(dark_pixels).rename('shadows')

    # Add dark pixels, cloud projection, and identified shadows as image bands.
    return img.addBands(ee.Image([dark_pixels, cld_proj, shadows]))
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
def add_cld_shdw_mask(img):
    # Add cloud component bands.
    img_cloud = add_cloud_bands(img)

    # Add cloud shadow component bands.
    img_cloud_shadow = add_shadow_bands(img_cloud)

    # Combine cloud and shadow mask, set cloud and shadow as value 1, else 0.
    is_cld_shdw = img_cloud_shadow.select('clouds').add(img_cloud_shadow.select('shadows')).gt(0)

    # Remove small cloud-shadow patches and dilate remaining pixels by BUFFER input.
    # 20 m scale is for speed, and assumes clouds don't require 10 m precision.
    is_cld_shdw = (is_cld_shdw.focalMin(2).focalMax(BUFFER*2/20)
        .reproject(**{'crs': img.select([0]).projection(), 'scale': 20})
        .rename('cloudmask'))

    # Add the final cloud-shadow mask to the image.
    return img_cloud_shadow.addBands(is_cld_shdw)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Import the folium library.
import folium

# Define a method for displaying Earth Engine image tiles to a folium map.
def add_ee_layer(self, ee_image_object, vis_params, name, show=True, opacity=1, min_zoom=0):
    map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
    folium.raster_layers.TileLayer(
        tiles=map_id_dict['tile_fetcher'].url_format,
        attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
        name=name,
        show=show,
        opacity=opacity,
        min_zoom=min_zoom,
        overlay=True,
        control=True
        ).add_to(self)

# Add the Earth Engine layer method to folium.
folium.Map.add_ee_layer = add_ee_layer
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
def display_cloud_layers(col):
    # Mosaic the image collection.
    img = col.mosaic()

    # Subset layers and prepare them for display.
    clouds = img.select('clouds').selfMask()
    shadows = img.select('shadows').selfMask()
    dark_pixels = img.select('dark_pixels').selfMask()
    probability = img.select('probability')
    cloudmask = img.select('cloudmask').selfMask()
    cloud_transform = img.select('cloud_transform')

    # Create a folium map object.
    center = Region.centroid(10).coordinates().reverse().getInfo()
    m = folium.Map(location=center, zoom_start=12)

    # Add layers to the folium map.
    m.add_ee_layer(img,
                   {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 2500, 'gamma': 1.1},
                   'S2 image', True, 1, 9)
    m.add_ee_layer(probability,
                   {'min': 0, 'max': 100},
                   'probability (cloud)', False, 1, 9)
    m.add_ee_layer(clouds,
                   {'palette': 'e056fd'},
                   'clouds', False, 1, 9)
    m.add_ee_layer(cloud_transform,
                   {'min': 0, 'max': 1, 'palette': ['white', 'black']},
                   'cloud_transform', False, 1, 9)
    m.add_ee_layer(dark_pixels,
                   {'palette': 'orange'},
                   'dark_pixels', False, 1, 9)
    m.add_ee_layer(shadows, {'palette': 'yellow'},
                   'shadows', False, 1, 9)
    m.add_ee_layer(cloudmask, {'palette': 'orange'},
                   'cloudmask', True, 0.5, 9)

    # Add a layer control panel to the map.
    m.add_child(folium.LayerControl())

    # Display the map.
    display(m)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
S2_SR_Cloud_Col_Eval_Disp = S2_SR_Cloud_Col_Eval.map(add_cld_shdw_mask)

display_cloud_layers(S2_SR_Cloud_Col_Eval_Disp)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.7.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_942e0bd6f047ee5fb221763c367767d4 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_942e0bd6f047ee5fb221763c367767d4&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_942e0bd6f047ee5fb221763c367767d4 = L.map(
                &quot;map_942e0bd6f047ee5fb221763c367767d4&quot;,
                {
                    center: [-12.536954984912139, 130.89427011089856],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_c402ae305755dbd1d2d038f0127f2d63 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_c402ae305755dbd1d2d038f0127f2d63.addTo(map_942e0bd6f047ee5fb221763c367767d4);

            var tile_layer_58c1c45351bd6b4a82335b2c4596af02 = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/a61965f9557fa122de4aa3778fc2f09c-1d8ad7846d9ca5868427322b6ac6e1e2/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_58c1c45351bd6b4a82335b2c4596af02.addTo(map_942e0bd6f047ee5fb221763c367767d4);

            var tile_layer_0606e7203be93ccef1be909b9f371fdc = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/35c33fc0ea636ae9c750fd0ec5562a4d-04dd0dd2a4dc6574294805d98a3ad999/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


            var tile_layer_5ff3e17322f44b3a17c2ae8ba0b6bcd5 = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/de11399a77290464626a42bb0cea790f-1a07ac64e12bc29c329db2624fc88612/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


            var tile_layer_4af2c35989e83d08025ca567d0b0d7c8 = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/b7163ca8d0a938f802fb365964464ed5-31eef8cf5a1034cf603196d02b06e701/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


            var tile_layer_6a10afc36d19af0b5a0ac75d1404a6bf = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/7d9a7c251eaefb4546cebe07286672cb-bde112f72d39a1e9326eb0705d5085de/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


            var tile_layer_bed40c7761a44d07d8f7a4890e996fc8 = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/9351a9198f353c5773ff32095b3a0238-598e2ffe4cc9e796257302efb28bbb87/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


            var tile_layer_966dd1df95205af4e8e0bf012161da6d = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/0c122aa3b679eec5eafd1ecbc3628758-85599b2bd43812139b4a5d18b5cded2b/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 0.5, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_966dd1df95205af4e8e0bf012161da6d.addTo(map_942e0bd6f047ee5fb221763c367767d4);

            var layer_control_fdc5cc4af75cfa02a6b97858da11e825_layers = {
                base_layers : {
                    &quot;openstreetmap&quot; : tile_layer_c402ae305755dbd1d2d038f0127f2d63,
                },
                overlays :  {
                    &quot;S2 image&quot; : tile_layer_58c1c45351bd6b4a82335b2c4596af02,
                    &quot;probability (cloud)&quot; : tile_layer_0606e7203be93ccef1be909b9f371fdc,
                    &quot;clouds&quot; : tile_layer_5ff3e17322f44b3a17c2ae8ba0b6bcd5,
                    &quot;cloud_transform&quot; : tile_layer_4af2c35989e83d08025ca567d0b0d7c8,
                    &quot;dark_pixels&quot; : tile_layer_6a10afc36d19af0b5a0ac75d1404a6bf,
                    &quot;shadows&quot; : tile_layer_bed40c7761a44d07d8f7a4890e996fc8,
                    &quot;cloudmask&quot; : tile_layer_966dd1df95205af4e8e0bf012161da6d,
                },
            };
            let layer_control_fdc5cc4af75cfa02a6b97858da11e825 = L.control.layers(
                layer_control_fdc5cc4af75cfa02a6b97858da11e825_layers.base_layers,
                layer_control_fdc5cc4af75cfa02a6b97858da11e825_layers.overlays,
                {&quot;autoZIndex&quot;: true, &quot;collapsed&quot;: true, &quot;position&quot;: &quot;topright&quot;}
            ).addTo(map_942e0bd6f047ee5fb221763c367767d4);


&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>


# **Remove Masking**


```python
Region = ee.Geometry.Rectangle(130.9825040586519,-12.591236530819916, 130.80603616314409,-12.482652274143653)
START_DATE = '2023-09-01'
END_DATE = '2023-09-02'
CLOUD_FILTER = 60
CLD_PRB_THRESH = 40
NIR_DRK_THRESH = 0.15
CLD_PRJ_DIST = 2
BUFFER = 100
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
S2_SR_Cloud_Col = Get_S2_SR_Cloud_Col(Region, START_DATE, END_DATE)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
def apply_cld_shdw_mask(img):
    # Subset the cloudmask band and invert it so clouds/shadow are 0, else 1.
    not_cld_shdw = img.select('cloudmask').Not()

    # Subset reflectance bands and update their masks, return the result.
    return img.select('B.*').updateMask(not_cld_shdw)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
S2_SR_Median = (S2_SR_Cloud_Col.map(add_cld_shdw_mask)
                             .map(apply_cld_shdw_mask)
                             .median())
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Create a folium map object.
center = Region.centroid(10).coordinates().reverse().getInfo()
m = folium.Map(location=center, zoom_start=12)

# Add layers to the folium map.
m.add_ee_layer(S2_SR_Median,
                {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 2500, 'gamma': 1.1},
                'S2 cloud-free mosaic', True, 1, 9)

# Add a layer control panel to the map.
m.add_child(folium.LayerControl())

# Display the map.
display(m)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.7.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_eb1fa65c78471871cd9ad0654185baef {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_eb1fa65c78471871cd9ad0654185baef&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_eb1fa65c78471871cd9ad0654185baef = L.map(
                &quot;map_eb1fa65c78471871cd9ad0654185baef&quot;,
                {
                    center: [-12.536954984912139, 130.89427011089856],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_b616fd251eca59599a6cbe2f6d110289 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_b616fd251eca59599a6cbe2f6d110289.addTo(map_eb1fa65c78471871cd9ad0654185baef);

            var tile_layer_55e4f5a5609066ca9bcfc90b4c582603 = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/d85d907caabed9bee74b80ae97b06075-b8cc982ddec7f70e54ad20b5e22a5860/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_55e4f5a5609066ca9bcfc90b4c582603.addTo(map_eb1fa65c78471871cd9ad0654185baef);

            var layer_control_237e866353763b6e62553f4981852131_layers = {
                base_layers : {
                    &quot;openstreetmap&quot; : tile_layer_b616fd251eca59599a6cbe2f6d110289,
                },
                overlays :  {
                    &quot;S2 cloud-free mosaic&quot; : tile_layer_55e4f5a5609066ca9bcfc90b4c582603,
                },
            };
            let layer_control_237e866353763b6e62553f4981852131 = L.control.layers(
                layer_control_237e866353763b6e62553f4981852131_layers.base_layers,
                layer_control_237e866353763b6e62553f4981852131_layers.overlays,
                {&quot;autoZIndex&quot;: true, &quot;collapsed&quot;: true, &quot;position&quot;: &quot;topright&quot;}
            ).addTo(map_eb1fa65c78471871cd9ad0654185baef);


&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>


# **Atmospheric Correction**


```python
#from google.colab import drive
#drive.mount('/content/drive')
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
#https://github.com/ridhodwid/gee-atmcorr-S2/blob/kaggle-usage/bin/atmospheric.py

import requests

url = "https://github.com/ridhodwid/gee-atmcorr-S2/blob/kaggle-usage/bin/atmospheric.py"
response = requests.get(url)

with open("filename", "wb") as file:
    file.write(response.content)

```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Import Modules

from Py6S import *
import datetime
import math
import os
import sys
sys.path.append('/content/drive/MyDrive/')
from atmospheric import Atmospheric
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
SixS
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>






    Py6S.sixs.SixS




```python
# Mark the Region of Interest
ROI= ee.Geometry.Rectangle(130.9825040586519,-12.591236530819916, 130.80603616314409,-12.482652274143653)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# The first Sentinel 2 image
S2_TOA = ee.Image(
  ee.ImageCollection('COPERNICUS/S2')
    .filterBounds(ROI)
    .filterDate('2023-09-01', '2023-09-02')
    .sort('CLOUDY_PIXEL_PERCENTAGE')
    .first()
  )

# top of atmosphere reflectance
TOA = S2_TOA.divide(10000)
display(S2_TOA)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<div><style>:root {
  --font-color-primary: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --font-color-secondary: var(--jp-content-font-color2, rgba(0, 0, 0, 0.6));
  --font-color-accent: rgba(123, 31, 162, 1);
  --border-color: var(--jp-border-color2, #e0e0e0);
  --background-color: var(--jp-layout-color0, white);
  --background-color-row-even: var(--jp-layout-color1, white);
  --background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme="dark"],
body[data-theme="dark"],
body.vscode-dark {
  --font-color-primary: rgba(255, 255, 255, 1);
  --font-color-secondary: rgba(255, 255, 255, 0.6);
  --font-color-accent: rgb(173, 132, 190);
  --border-color: #2e2e2e;
  --background-color: #111111;
  --background-color-row-even: #111111;
  --background-color-row-odd: #313131;
}

.ee {
  padding: 1em;
  line-height: 1.5em;
  min-width: 300px;
  max-width: 1200px;
  overflow-y: scroll;
  max-height: 600px;
  border: 1px solid var(--border-color);
  font-family: monospace;
}

.ee li {
  list-style-type: none;
}

.ee ul {
  padding-left: 1.5em !important;
  margin: 0;
}

.ee > ul {
  padding-left: 0 !important;
}

.ee-open,
.ee-shut {
  color: var(--font-color-secondary);
  cursor: pointer;
  margin: 0;
}

.ee-open:hover,
.ee-shut:hover {
  color: var(--font-color-primary);
}

.ee-k {
  color: var(--font-color-accent);
  margin-right: 6px;
}

.ee-v {
  color: var(--font-color-primary);
}

.ee-toggle {
  display: none;
}

.ee-shut + ul {
  display: none;
}

.ee-open + ul {
  display: block;
}

.ee-shut::before {
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transform: rotate(-90deg);
  transition: transform 0.2s;
}

.ee-open::before {
  transform: rotate(0deg);
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transition: transform 0.2s;
}
</style><div class='ee'><ul><li><label class='ee-shut'>Image COPERNICUS/S2/20230901T013701_20230901T013903_T52LGM (16 bands)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>Image</span></li><li><span class='ee-k'>id:</span><span class='ee-v'>COPERNICUS/S2/20230901T013701_20230901T013903_T52LGM</span></li><li><span class='ee-k'>version:</span><span class='ee-v'>1693565197459558</span></li><li><label class='ee-shut'>bands: List (16 elements)<input type='checkbox' class='ee-toggle'></label><ul><li><label class='ee-shut'>0: "B1", unsigned int16, EPSG:32752, 1830x1830 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B1</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [60, 0, 699960, 0, -60, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>60</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-60</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [1830, 1830]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>1830</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>1830</span></li></ul></li></ul></li><li><label class='ee-shut'>1: "B2", unsigned int16, EPSG:32752, 10980x10980 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B2</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [10, 0, 699960, 0, -10, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-10</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [10980, 10980]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10980</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>10980</span></li></ul></li></ul></li><li><label class='ee-shut'>2: "B3", unsigned int16, EPSG:32752, 10980x10980 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B3</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [10, 0, 699960, 0, -10, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-10</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [10980, 10980]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10980</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>10980</span></li></ul></li></ul></li><li><label class='ee-shut'>3: "B4", unsigned int16, EPSG:32752, 10980x10980 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B4</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [10, 0, 699960, 0, -10, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-10</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [10980, 10980]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10980</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>10980</span></li></ul></li></ul></li><li><label class='ee-shut'>4: "B5", unsigned int16, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B5</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li><li><label class='ee-shut'>5: "B6", unsigned int16, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B6</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li><li><label class='ee-shut'>6: "B7", unsigned int16, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B7</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li><li><label class='ee-shut'>7: "B8", unsigned int16, EPSG:32752, 10980x10980 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B8</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [10, 0, 699960, 0, -10, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-10</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [10980, 10980]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10980</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>10980</span></li></ul></li></ul></li><li><label class='ee-shut'>8: "B8A", unsigned int16, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B8A</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li><li><label class='ee-shut'>9: "B9", unsigned int16, EPSG:32752, 1830x1830 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B9</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [60, 0, 699960, 0, -60, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>60</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-60</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [1830, 1830]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>1830</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>1830</span></li></ul></li></ul></li><li><label class='ee-shut'>10: "B10", unsigned int16, EPSG:32752, 1830x1830 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B10</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [60, 0, 699960, 0, -60, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>60</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-60</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [1830, 1830]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>1830</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>1830</span></li></ul></li></ul></li><li><label class='ee-shut'>11: "B11", unsigned int16, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B11</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li><li><label class='ee-shut'>12: "B12", unsigned int16, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B12</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li><li><label class='ee-shut'>13: "QA10", unsigned int16, EPSG:32752, 10980x10980 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>QA10</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [10, 0, 699960, 0, -10, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-10</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [10980, 10980]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>10980</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>10980</span></li></ul></li></ul></li><li><label class='ee-shut'>14: "QA20", unsigned int32, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>QA20</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int32<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>4294967295</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li><li><label class='ee-shut'>15: "QA60", unsigned int16, EPSG:32752, 1830x1830 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>QA60</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [60, 0, 699960, 0, -60, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>60</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-60</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: unsigned int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>65535</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [1830, 1830]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>1830</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>1830</span></li></ul></li></ul></li></ul></li><li><label class='ee-shut'>properties: Object (80 properties)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>CLOUDY_PIXEL_PERCENTAGE:</span><span class='ee-v'>0.150724219390079</span></li><li><span class='ee-k'>CLOUD_COVERAGE_ASSESSMENT:</span><span class='ee-v'>0.150724219390079</span></li><li><span class='ee-k'>DATASTRIP_ID:</span><span class='ee-v'>S2A_OPER_MSI_L1C_DS_2APS_20230901T053509_S20230901T013903_N05.09</span></li><li><span class='ee-k'>DATATAKE_IDENTIFIER:</span><span class='ee-v'>GS2A_20230901T013701_042785_N05.09</span></li><li><span class='ee-k'>DATATAKE_TYPE:</span><span class='ee-v'>INS-NOBS</span></li><li><span class='ee-k'>DEGRADED_MSI_DATA_PERCENTAGE:</span><span class='ee-v'>0.0224</span></li><li><span class='ee-k'>FORMAT_CORRECTNESS:</span><span class='ee-v'>PASSED</span></li><li><span class='ee-k'>GENERAL_QUALITY:</span><span class='ee-v'>PASSED</span></li><li><span class='ee-k'>GENERATION_TIME:</span><span class='ee-v'>1693546509000</span></li><li><span class='ee-k'>GEOMETRIC_QUALITY:</span><span class='ee-v'>PASSED</span></li><li><span class='ee-k'>GRANULE_ID:</span><span class='ee-v'>L1C_T52LGM_A042785_20230901T013903</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B1:</span><span class='ee-v'>285.231930615425</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B10:</span><span class='ee-v'>284.961244698558</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B11:</span><span class='ee-v'>285.093674288642</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B12:</span><span class='ee-v'>285.213791421383</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B2:</span><span class='ee-v'>284.850706285815</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B3:</span><span class='ee-v'>284.965751559356</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B4:</span><span class='ee-v'>285.051516222862</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B5:</span><span class='ee-v'>285.078221847574</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B6:</span><span class='ee-v'>285.131138999988</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B7:</span><span class='ee-v'>285.167277742866</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B8:</span><span class='ee-v'>284.909250833345</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B8A:</span><span class='ee-v'>285.216068513189</span></li><li><span class='ee-k'>MEAN_INCIDENCE_AZIMUTH_ANGLE_B9:</span><span class='ee-v'>285.238908010118</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B1:</span><span class='ee-v'>7.67574437330261</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B10:</span><span class='ee-v'>7.51109901074545</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B11:</span><span class='ee-v'>7.56803683526518</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B12:</span><span class='ee-v'>7.6533662651218</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B2:</span><span class='ee-v'>7.45309917494876</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B3:</span><span class='ee-v'>7.48375030369673</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B4:</span><span class='ee-v'>7.52294677522075</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B5:</span><span class='ee-v'>7.5437437831719</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B6:</span><span class='ee-v'>7.57182188975002</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B7:</span><span class='ee-v'>7.60269868488235</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B8:</span><span class='ee-v'>7.46690837545628</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B8A:</span><span class='ee-v'>7.6363408940446</span></li><li><span class='ee-k'>MEAN_INCIDENCE_ZENITH_ANGLE_B9:</span><span class='ee-v'>7.71282983185552</span></li><li><span class='ee-k'>MEAN_SOLAR_AZIMUTH_ANGLE:</span><span class='ee-v'>49.615814634594</span></li><li><span class='ee-k'>MEAN_SOLAR_ZENITH_ANGLE:</span><span class='ee-v'>31.1936641036077</span></li><li><span class='ee-k'>MGRS_TILE:</span><span class='ee-v'>52LGM</span></li><li><span class='ee-k'>PROCESSING_BASELINE:</span><span class='ee-v'>05.09</span></li><li><span class='ee-k'>PRODUCT_ID:</span><span class='ee-v'>S2A_MSIL1C_20230901T013701_N0509_R031_T52LGM_20230901T053509</span></li><li><span class='ee-k'>RADIOMETRIC_QUALITY:</span><span class='ee-v'>PASSED</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B1:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B10:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B11:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B12:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B2:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B3:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B4:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B5:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B6:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B7:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B8:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B8A:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>RADIO_ADD_OFFSET_B9:</span><span class='ee-v'>-1000</span></li><li><span class='ee-k'>REFLECTANCE_CONVERSION_CORRECTION:</span><span class='ee-v'>0.980220821504379</span></li><li><span class='ee-k'>SENSING_ORBIT_DIRECTION:</span><span class='ee-v'>DESCENDING</span></li><li><span class='ee-k'>SENSING_ORBIT_NUMBER:</span><span class='ee-v'>31</span></li><li><span class='ee-k'>SENSOR_QUALITY:</span><span class='ee-v'>PASSED</span></li><li><span class='ee-k'>SNOW_PIXEL_PERCENTAGE:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B1:</span><span class='ee-v'>1884.69</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B10:</span><span class='ee-v'>367.15</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B11:</span><span class='ee-v'>245.59</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B12:</span><span class='ee-v'>85.25</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B2:</span><span class='ee-v'>1959.66</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B3:</span><span class='ee-v'>1823.24</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B4:</span><span class='ee-v'>1512.06</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B5:</span><span class='ee-v'>1424.64</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B6:</span><span class='ee-v'>1287.61</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B7:</span><span class='ee-v'>1162.08</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B8:</span><span class='ee-v'>1041.63</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B8A:</span><span class='ee-v'>955.32</span></li><li><span class='ee-k'>SOLAR_IRRADIANCE_B9:</span><span class='ee-v'>812.92</span></li><li><span class='ee-k'>SPACECRAFT_NAME:</span><span class='ee-v'>Sentinel-2A</span></li><li><span class='ee-k'>system:asset_size:</span><span class='ee-v'>1057480333</span></li><li><label class='ee-shut'>system:footprint: LinearRing (22 vertices)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>LinearRing</span></li><li><label class='ee-shut'>coordinates: List (22 elements)<input type='checkbox' class='ee-toggle'></label><ul><li><label class='ee-shut'>0: [131.84163506914214, -11.74526553620342]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.84163506914214</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.74526553620342</span></li></ul></li><li><label class='ee-shut'>1: [131.84161998193966, -11.745262856878322]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.84161998193966</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.745262856878322</span></li></ul></li><li><label class='ee-shut'>2: [130.8349298285638, -11.753511370486487]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.8349298285638</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.753511370486487</span></li></ul></li><li><label class='ee-shut'>3: [130.83488775601666, -11.75354817608379]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.83488775601666</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.75354817608379</span></li></ul></li><li><label class='ee-shut'>4: [130.83483842688074, -11.753581562325733]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.83483842688074</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.753581562325733</span></li></ul></li><li><label class='ee-shut'>5: [130.83819880969662, -12.249736806680732]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.83819880969662</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.249736806680732</span></li></ul></li><li><label class='ee-shut'>6: [130.84170889521266, -12.74585280811192]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.84170889521266</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.74585280811192</span></li></ul></li><li><label class='ee-shut'>7: [130.84174664021972, -12.745894025964619]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.84174664021972</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.745894025964619</span></li></ul></li><li><label class='ee-shut'>8: [130.84178091173834, -12.745942307726853]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.84178091173834</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.745942307726853</span></li></ul></li><li><label class='ee-shut'>9: [131.7313430193807, -12.738251805352146]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.7313430193807</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.738251805352146</span></li></ul></li><li><label class='ee-shut'>10: [131.7313728752351, -12.738225629736172]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.7313728752351</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.738225629736172</span></li></ul></li><li><label class='ee-shut'>11: [131.73141253107752, -12.738219906796223]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.73141253107752</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.738219906796223</span></li></ul></li><li><label class='ee-shut'>12: [131.73142514193324, -12.73820101733667]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.73142514193324</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.73820101733667</span></li></ul></li><li><label class='ee-shut'>13: [131.73160845482576, -12.737831422845746]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.73160845482576</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.737831422845746</span></li></ul></li><li><label class='ee-shut'>14: [131.74655325600176, -12.689607997564122]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.74655325600176</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.689607997564122</span></li></ul></li><li><label class='ee-shut'>15: [131.79644873004426, -12.454310391471406]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.79644873004426</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.454310391471406</span></li></ul></li><li><label class='ee-shut'>16: [131.8462982538301, -12.219022224724002]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.8462982538301</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.219022224724002</span></li></ul></li><li><label class='ee-shut'>17: [131.8466481091617, -12.217202494548483]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.8466481091617</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.217202494548483</span></li></ul></li><li><label class='ee-shut'>18: [131.8441504033828, -11.98127507798823]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.8441504033828</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.98127507798823</span></li></ul></li><li><label class='ee-shut'>19: [131.84170512222843, -11.745351998147404]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.84170512222843</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.745351998147404</span></li></ul></li><li><label class='ee-shut'>20: [131.8416672905405, -11.745310955045383]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.8416672905405</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.745310955045383</span></li></ul></li><li><label class='ee-shut'>21: [131.84163506914214, -11.74526553620342]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>131.84163506914214</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-11.74526553620342</span></li></ul></li></ul></li></ul></li><li><span class='ee-k'>system:index:</span><span class='ee-v'>20230901T013701_20230901T013903_T52LGM</span></li><li><span class='ee-k'>system:time_end:</span><span class='ee-v'>1693532448740</span></li><li><span class='ee-k'>system:time_start:</span><span class='ee-v'>1693532448740</span></li></ul></li></ul></li></ul></div><script>function toggleHeader() {
    const parent = this.parentElement;
    parent.className = parent.className === "ee-open" ? "ee-shut" : "ee-open";
}

for (let c of document.getElementsByClassName("ee-toggle")) {
    c.onclick = toggleHeader;
}</script></div>



```python
info = S2_TOA.getInfo()['properties']
scene_date = datetime.datetime.utcfromtimestamp(info['system:time_start']/1000)# i.e. Python uses seconds, EE uses milliseconds
solar_z = info['MEAN_SOLAR_ZENITH_ANGLE']
date = ee.Date(scene_date.strftime("%Y-%m-%d"))
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
h2o = Atmospheric.water(ROI,date).getInfo()
o3 = Atmospheric.ozone(ROI,date).getInfo()
aot = Atmospheric.aerosol(ROI,date).getInfo()
display(h2o,o3,aot)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




    1.8299999237060547



    0.274



    0.22833332419395447



```python
# Calculate target altitude in km
SRTM = ee.Image('CGIAR/SRTM90_V4') # Shuttle Radar Topography mission covers *most* of the Earth
alt = SRTM.reduceRegion(reducer = ee.Reducer.mean(),geometry = ROI.centroid()).get('elevation').getInfo()
km = alt/1000 # i.e. Py6S uses units of kilometers
display(SRTM,alt,km)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<div><style>:root {
  --font-color-primary: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --font-color-secondary: var(--jp-content-font-color2, rgba(0, 0, 0, 0.6));
  --font-color-accent: rgba(123, 31, 162, 1);
  --border-color: var(--jp-border-color2, #e0e0e0);
  --background-color: var(--jp-layout-color0, white);
  --background-color-row-even: var(--jp-layout-color1, white);
  --background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme="dark"],
body[data-theme="dark"],
body.vscode-dark {
  --font-color-primary: rgba(255, 255, 255, 1);
  --font-color-secondary: rgba(255, 255, 255, 0.6);
  --font-color-accent: rgb(173, 132, 190);
  --border-color: #2e2e2e;
  --background-color: #111111;
  --background-color-row-even: #111111;
  --background-color-row-odd: #313131;
}

.ee {
  padding: 1em;
  line-height: 1.5em;
  min-width: 300px;
  max-width: 1200px;
  overflow-y: scroll;
  max-height: 600px;
  border: 1px solid var(--border-color);
  font-family: monospace;
}

.ee li {
  list-style-type: none;
}

.ee ul {
  padding-left: 1.5em !important;
  margin: 0;
}

.ee > ul {
  padding-left: 0 !important;
}

.ee-open,
.ee-shut {
  color: var(--font-color-secondary);
  cursor: pointer;
  margin: 0;
}

.ee-open:hover,
.ee-shut:hover {
  color: var(--font-color-primary);
}

.ee-k {
  color: var(--font-color-accent);
  margin-right: 6px;
}

.ee-v {
  color: var(--font-color-primary);
}

.ee-toggle {
  display: none;
}

.ee-shut + ul {
  display: none;
}

.ee-open + ul {
  display: block;
}

.ee-shut::before {
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transform: rotate(-90deg);
  transition: transform 0.2s;
}

.ee-open::before {
  transform: rotate(0deg);
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transition: transform 0.2s;
}
</style><div class='ee'><ul><li><label class='ee-shut'>Image CGIAR/SRTM90_V4 (1 band)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>Image</span></li><li><span class='ee-k'>id:</span><span class='ee-v'>CGIAR/SRTM90_V4</span></li><li><span class='ee-k'>version:</span><span class='ee-v'>1641990053291277</span></li><li><label class='ee-shut'>bands: List (1 element)<input type='checkbox' class='ee-toggle'></label><ul><li><label class='ee-shut'>0: "elevation", signed int16, EPSG:4326, 432000x144000 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>elevation</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:4326</span></li><li><label class='ee-shut'>crs_transform: List (6 elements)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>0.000833333333333</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>-180</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-0.000833333333333</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>60</span></li></ul></li><li><label class='ee-shut'>data_type: signed int16<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>32767</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>-32768</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>int</span></li></ul></li><li><label class='ee-shut'>dimensions: [432000, 144000]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>432000</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>144000</span></li></ul></li></ul></li></ul></li><li><label class='ee-shut'>properties: Object (25 properties)<input type='checkbox' class='ee-toggle'></label><ul><li><label class='ee-shut'>date_range: [950227200000, 951177600000]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>950227200000</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>951177600000</span></li></ul></li><li><span class='ee-k'>description:</span><span class='ee-v'><p>The Shuttle Radar Topography Mission (SRTM) digital
elevation dataset was originally produced to provide consistent,
high-quality elevation data at near global scope. This version
of the SRTM digital elevation data has been processed to fill data
voids, and to facilitate its ease of use.</p><p><b>Provider: <a href="https://srtm.csi.cgiar.org/">NASA/CGIAR</a></b><br><p><b>Bands</b><table class="eecat"><tr><th scope="col">Name</th><th scope="col">Description</th></tr><tr><td>elevation</td><td><p>Elevation</p></td></tr></table><p><b>Terms of Use</b><br><p>DISTRIBUTION. Users are prohibited from any commercial, non-free resale, or
redistribution without explicit written permission from CIAT. Users should
acknowledge CIAT as the source used in the creation of any reports,
publications, new datasets, derived products, or services resulting from the
use of this dataset. CIAT also request reprints of any publications and
notification of any redistributing efforts. For commercial access to
the data, send requests to <a href="mailto:a.jarvis@cgiar.org">Andy Jarvis</a>.</p><p>NO WARRANTY OR LIABILITY. CIAT provides these data without any warranty of
any kind whatsoever, either express or implied, including warranties of
merchantability and fitness for a particular purpose. CIAT shall not be
liable for incidental, consequential, or special damages arising out of
the use of any data.</p><p>ACKNOWLEDGMENT AND CITATION. Any users are kindly asked to cite this data
in any published material produced using this data, and if possible link
web pages to the <a href="https://srtm.csi.cgiar.org">CIAT-CSI SRTM website</a>.</p><p><b>Suggested citation(s)</b><ul><li><p>Jarvis, A., H.I. Reuter, A. Nelson, E. Guevara. 2008. Hole-filled
SRTM for the globe Version 4, available from the CGIAR-CSI SRTM
90m Database: https://srtm.csi.cgiar.org.</p></li></ul><style>
  table.eecat {
  border: 1px solid black;
  border-collapse: collapse;
  font-size: 13px;
  }
  table.eecat td, tr, th {
  text-align: left; vertical-align: top;
  border: 1px solid gray; padding: 3px;
  }
  td.nobreak { white-space: nowrap; }
</style></span></li><li><label class='ee-shut'>keywords: List (6 elements)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>cgiar</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>dem</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>elevation</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>geophysical</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>srtm</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>topography</span></li></ul></li><li><span class='ee-k'>period:</span><span class='ee-v'>0</span></li><li><label class='ee-shut'>product_tags: List (5 elements)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>srtm</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>elevation</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>topography</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>dem</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>geophysical</span></li></ul></li><li><span class='ee-k'>provider:</span><span class='ee-v'>NASA/CGIAR</span></li><li><span class='ee-k'>provider_url:</span><span class='ee-v'>https://srtm.csi.cgiar.org/</span></li><li><span class='ee-k'>sample:</span><span class='ee-v'>https://mw1.google.com/ges/dd/images/SRTM90_V4_sample.png</span></li><li><label class='ee-shut'>source_tags: ['cgiar']<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>cgiar</span></li></ul></li><li><span class='ee-k'>system:asset_size:</span><span class='ee-v'>18827626666</span></li><li><span class='ee-k'>system:time_end:</span><span class='ee-v'>951177600000</span></li><li><span class='ee-k'>system:time_start:</span><span class='ee-v'>950227200000</span></li><li><span class='ee-k'>system:visualization_0_bands:</span><span class='ee-v'>elevation</span></li><li><span class='ee-k'>system:visualization_0_gamma:</span><span class='ee-v'>1.6</span></li><li><span class='ee-k'>system:visualization_0_max:</span><span class='ee-v'>8000.0</span></li><li><span class='ee-k'>system:visualization_0_min:</span><span class='ee-v'>-100.0</span></li><li><span class='ee-k'>system:visualization_0_name:</span><span class='ee-v'>Elevation</span></li><li><label class='ee-shut'>tags: List (6 elements)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>cgiar</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>dem</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>elevation</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>geophysical</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>srtm</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>topography</span></li></ul></li><li><span class='ee-k'>thumb:</span><span class='ee-v'>https://mw1.google.com/ges/dd/images/SRTM90_V4_thumb.png</span></li><li><span class='ee-k'>title:</span><span class='ee-v'>SRTM Digital Elevation Data Version 4</span></li><li><span class='ee-k'>type_name:</span><span class='ee-v'>Image</span></li><li><span class='ee-k'>visualization_0_bands:</span><span class='ee-v'>elevation</span></li><li><span class='ee-k'>visualization_0_max:</span><span class='ee-v'>8000.0</span></li><li><span class='ee-k'>visualization_0_min:</span><span class='ee-v'>-100.0</span></li><li><span class='ee-k'>visualization_0_name:</span><span class='ee-v'>Elevation</span></li></ul></li></ul></li></ul></div><script>function toggleHeader() {
    const parent = this.parentElement;
    parent.className = parent.className === "ee-open" ? "ee-shut" : "ee-open";
}

for (let c of document.getElementsByClassName("ee-toggle")) {
    c.onclick = toggleHeader;
}</script></div>



    9



    0.009



```python
# Instantiate
s = SixS()

# Atmospheric constituents
s.atmos_profile = AtmosProfile.UserWaterAndOzone(h2o,o3)
s.aero_profile = AeroProfile.Continental
s.aot550 = aot

# Earth-Sun-satellite geometry
s.geometry = Geometry.User()
s.geometry.view_z = 0               # always NADIR (I think..)
s.geometry.solar_z = solar_z        # solar zenith angle
s.geometry.month = scene_date.month # month and day used for Earth-Sun distance
s.geometry.day = scene_date.day     # month and day used for Earth-Sun distance
s.altitudes.set_sensor_satellite_level()
s.altitudes.set_target_custom_altitude(km)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Spectral Response Functions
# To obtain the spectral response fx of each band

def spectralResponseFunction(bandname):
    """
    Extract spectral response function for given band name
    """

    bandSelect = {
        'B1':PredefinedWavelengths.S2A_MSI_01,
        'B2':PredefinedWavelengths.S2A_MSI_02,
        'B3':PredefinedWavelengths.S2A_MSI_03,
        'B4':PredefinedWavelengths.S2A_MSI_04,
        'B5':PredefinedWavelengths.S2A_MSI_05,
        'B6':PredefinedWavelengths.S2A_MSI_06,
        'B7':PredefinedWavelengths.S2A_MSI_07,
        'B8':PredefinedWavelengths.S2A_MSI_08,
        'B8A':PredefinedWavelengths.S2A_MSI_8A,
        'B9':PredefinedWavelengths.S2A_MSI_09,
        'B10':PredefinedWavelengths.S2A_MSI_10,
        'B11':PredefinedWavelengths.S2A_MSI_11,
        'B12':PredefinedWavelengths.S2A_MSI_12,
        }

    return Wavelength(bandSelect[bandname])
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# TOA Reflectance to Radiance
def TOA_to_rad(bandname):
    """
    Converts top of atmosphere reflectance to at-sensor radiance
    """

    # solar exoatmospheric spectral irradiance
    ESUN = info['SOLAR_IRRADIANCE_'+bandname]
    solar_angle_correction = math.cos(math.radians(solar_z))

    # Earth-Sun distance (from day of year)
    doy = scene_date.timetuple().tm_yday
    d = 1 - 0.01672 * math.cos(0.9856 * (doy-4)) # From http://physics.stackexchange.com/questions/177949/earth-sun-distance-on-a-given-day-of-the-year

    # conversion factor
    multiplier = ESUN*solar_angle_correction/(math.pi*d**2)

    # at-sensor radiance
    rad = TOA.select(bandname).multiply(multiplier)

    return rad
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Radiance to Surface Reflectance
def surface_reflectance(bandname):
    """
    Calculate surface reflectance from at-sensor radiance given waveband name
    """

    # run 6S for this waveband
    s.wavelength = spectralResponseFunction(bandname)
    s.run()

    # extract 6S outputs
    Edir = s.outputs.direct_solar_irradiance             #direct solar irradiance
    Edif = s.outputs.diffuse_solar_irradiance            #diffuse solar irradiance
    Lp   = s.outputs.atmospheric_intrinsic_radiance      #path radiance
    absorb  = s.outputs.trans['global_gas'].upward       #absorption transmissivity
    scatter = s.outputs.trans['total_scattering'].upward #scattering transmissivity
    tau2 = absorb*scatter                                #total transmissivity

    # radiance to surface reflectance
    rad = TOA_to_rad(bandname)
    ref = rad.subtract(Lp).multiply(math.pi).divide(tau2*(Edir+Edif))


    return ref
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Use this if you only need surface reflectance of rgb channel
b = surface_reflectance('B8')
g = surface_reflectance('B11')
r = surface_reflectance('B12')
ref = r.addBands(g).addBands(b)

# Calculate surface reflectance for all wavebands
output = S2_TOA.select('QA60')
for band in ['B1','B2','B3','B4','B5','B6','B7','B8','B8A','B9','B10','B11','B12']:
    print(band)
    band_reflectance = surface_reflectance(band)
    output = output.addBands(surface_reflectance(band))
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



    B1
    B2
    B3
    B4
    B5
    B6
    B7
    B8
    B8A
    B9
    B10
    B11
    B12
    


```python
# select band of interest
band11 = ref.select('B11')
band12 = ref.select('B12')

display(band11,band12)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<div><style>:root {
  --font-color-primary: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --font-color-secondary: var(--jp-content-font-color2, rgba(0, 0, 0, 0.6));
  --font-color-accent: rgba(123, 31, 162, 1);
  --border-color: var(--jp-border-color2, #e0e0e0);
  --background-color: var(--jp-layout-color0, white);
  --background-color-row-even: var(--jp-layout-color1, white);
  --background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme="dark"],
body[data-theme="dark"],
body.vscode-dark {
  --font-color-primary: rgba(255, 255, 255, 1);
  --font-color-secondary: rgba(255, 255, 255, 0.6);
  --font-color-accent: rgb(173, 132, 190);
  --border-color: #2e2e2e;
  --background-color: #111111;
  --background-color-row-even: #111111;
  --background-color-row-odd: #313131;
}

.ee {
  padding: 1em;
  line-height: 1.5em;
  min-width: 300px;
  max-width: 1200px;
  overflow-y: scroll;
  max-height: 600px;
  border: 1px solid var(--border-color);
  font-family: monospace;
}

.ee li {
  list-style-type: none;
}

.ee ul {
  padding-left: 1.5em !important;
  margin: 0;
}

.ee > ul {
  padding-left: 0 !important;
}

.ee-open,
.ee-shut {
  color: var(--font-color-secondary);
  cursor: pointer;
  margin: 0;
}

.ee-open:hover,
.ee-shut:hover {
  color: var(--font-color-primary);
}

.ee-k {
  color: var(--font-color-accent);
  margin-right: 6px;
}

.ee-v {
  color: var(--font-color-primary);
}

.ee-toggle {
  display: none;
}

.ee-shut + ul {
  display: none;
}

.ee-open + ul {
  display: block;
}

.ee-shut::before {
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transform: rotate(-90deg);
  transition: transform 0.2s;
}

.ee-open::before {
  transform: rotate(0deg);
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transition: transform 0.2s;
}
</style><div class='ee'><ul><li><label class='ee-shut'>Image (1 band)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>Image</span></li><li><label class='ee-shut'>bands: List (1 element)<input type='checkbox' class='ee-toggle'></label><ul><li><label class='ee-shut'>0: "B11", double, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B11</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: double<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>7.1709430269334815</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>-0.003724724487949203</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>double</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li></ul></li></ul></li></ul></div><script>function toggleHeader() {
    const parent = this.parentElement;
    parent.className = parent.className === "ee-open" ? "ee-shut" : "ee-open";
}

for (let c of document.getElementsByClassName("ee-toggle")) {
    c.onclick = toggleHeader;
}</script></div>



<div><style>:root {
  --font-color-primary: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --font-color-secondary: var(--jp-content-font-color2, rgba(0, 0, 0, 0.6));
  --font-color-accent: rgba(123, 31, 162, 1);
  --border-color: var(--jp-border-color2, #e0e0e0);
  --background-color: var(--jp-layout-color0, white);
  --background-color-row-even: var(--jp-layout-color1, white);
  --background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme="dark"],
body[data-theme="dark"],
body.vscode-dark {
  --font-color-primary: rgba(255, 255, 255, 1);
  --font-color-secondary: rgba(255, 255, 255, 0.6);
  --font-color-accent: rgb(173, 132, 190);
  --border-color: #2e2e2e;
  --background-color: #111111;
  --background-color-row-even: #111111;
  --background-color-row-odd: #313131;
}

.ee {
  padding: 1em;
  line-height: 1.5em;
  min-width: 300px;
  max-width: 1200px;
  overflow-y: scroll;
  max-height: 600px;
  border: 1px solid var(--border-color);
  font-family: monospace;
}

.ee li {
  list-style-type: none;
}

.ee ul {
  padding-left: 1.5em !important;
  margin: 0;
}

.ee > ul {
  padding-left: 0 !important;
}

.ee-open,
.ee-shut {
  color: var(--font-color-secondary);
  cursor: pointer;
  margin: 0;
}

.ee-open:hover,
.ee-shut:hover {
  color: var(--font-color-primary);
}

.ee-k {
  color: var(--font-color-accent);
  margin-right: 6px;
}

.ee-v {
  color: var(--font-color-primary);
}

.ee-toggle {
  display: none;
}

.ee-shut + ul {
  display: none;
}

.ee-open + ul {
  display: block;
}

.ee-shut::before {
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transform: rotate(-90deg);
  transition: transform 0.2s;
}

.ee-open::before {
  transform: rotate(0deg);
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transition: transform 0.2s;
}
</style><div class='ee'><ul><li><label class='ee-shut'>Image (1 band)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>Image</span></li><li><label class='ee-shut'>bands: List (1 element)<input type='checkbox' class='ee-toggle'></label><ul><li><label class='ee-shut'>0: "B12", double, EPSG:32752, 5490x5490 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B12</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8700040]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8700040</span></li></ul></li><li><label class='ee-shut'>data_type: double<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>max:</span><span class='ee-v'>7.748684484853874</span></li><li><span class='ee-k'>min:</span><span class='ee-v'>-0.0014553630981165304</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>double</span></li></ul></li><li><label class='ee-shut'>dimensions: [5490, 5490]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>5490</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>5490</span></li></ul></li></ul></li></ul></li></ul></li></ul></div><script>function toggleHeader() {
    const parent = this.parentElement;
    parent.className = parent.className === "ee-open" ? "ee-shut" : "ee-open";
}

for (let c of document.getElementsByClassName("ee-toggle")) {
    c.onclick = toggleHeader;
}</script></div>



```python
# Create a folium map object.
center = ROI.centroid(10).coordinates().reverse().getInfo()
S2_AC = folium.Map(location=center, zoom_start=12)

# Add layers to the folium map.
S2_AC.add_ee_layer(band11,
                {'min': 0, 'max': 0.3, 'gamma': 3},
                'S2_Band11', True, 1, 9)

# Add layers to the folium map.
S2_AC.add_ee_layer(band12,
                {'min': 0, 'max': 0.3, 'gamma': 3},
                'S2_Band12',True, 1, 9)

# Add a layer control panel to the map.
S2_AC.add_child(folium.LayerControl())

# Display the map.
display(S2_AC)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;

    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;

        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;

    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.7.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;

            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_a4b61c17274732a98da0dcb32f602730 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;

&lt;/head&gt;
&lt;body&gt;


            &lt;div class=&quot;folium-map&quot; id=&quot;map_a4b61c17274732a98da0dcb32f602730&quot; &gt;&lt;/div&gt;

&lt;/body&gt;
&lt;script&gt;


            var map_a4b61c17274732a98da0dcb32f602730 = L.map(
                &quot;map_a4b61c17274732a98da0dcb32f602730&quot;,
                {
                    center: [-12.536954984912139, 130.89427011089856],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );





            var tile_layer_1a151692c3d7969c6c0d8fadf3540ce0 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_1a151692c3d7969c6c0d8fadf3540ce0.addTo(map_a4b61c17274732a98da0dcb32f602730);

            var tile_layer_89d4ad24e95d8780add57f74d189d01f = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/889c218e7941d4a86cf908d341e369e1-088504fd24e22aaf0c4222684a3d2999/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_89d4ad24e95d8780add57f74d189d01f.addTo(map_a4b61c17274732a98da0dcb32f602730);

            var tile_layer_f904eb06792b1c2716635c9d63a9f994 = L.tileLayer(
                &quot;https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/d6fbc7c17987d14cfd86b4cf3e781bd7-7cfca37cf4afac4d80cb5c45bdbc4f74/tiles/{z}/{x}/{y}&quot;,
                {&quot;attribution&quot;: &quot;Map Data \u0026copy; \u003ca href=\&quot;https://earthengine.google.com/\&quot;\u003eGoogle Earth Engine\u003c/a\u003e&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 9, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            );


                tile_layer_f904eb06792b1c2716635c9d63a9f994.addTo(map_a4b61c17274732a98da0dcb32f602730);

            var layer_control_882b34e565ae056d237883a0be5e1c0f_layers = {
                base_layers : {
                    &quot;openstreetmap&quot; : tile_layer_1a151692c3d7969c6c0d8fadf3540ce0,
                },
                overlays :  {
                    &quot;S2_Band11&quot; : tile_layer_89d4ad24e95d8780add57f74d189d01f,
                    &quot;S2_Band12&quot; : tile_layer_f904eb06792b1c2716635c9d63a9f994,
                },
            };
            let layer_control_882b34e565ae056d237883a0be5e1c0f = L.control.layers(
                layer_control_882b34e565ae056d237883a0be5e1c0f_layers.base_layers,
                layer_control_882b34e565ae056d237883a0be5e1c0f_layers.overlays,
                {&quot;autoZIndex&quot;: true, &quot;collapsed&quot;: true, &quot;position&quot;: &quot;topright&quot;}
            ).addTo(map_a4b61c17274732a98da0dcb32f602730);


&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>


# **Save Image as Tif by Exporting to Drive**


```python
# Get the folium map as an image
image = geemap.Map.to_image(S2_AC)

# Display the image
print("Captured Image:", image)
display(image)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



    Captured Image: None
    


    None



```python
# Export the clipped image to Google Drive as a GeoTIFF file
export_params = {
    'image': S2_TOA.select(['B11', 'B12']),
    'description': 'Sentinel_AC',
    'scale': 10,
    'region': ROI,
    'fileFormat': 'GeoTIFF',  # Specify the file format
}

# Export the image
task = ee.batch.Export.image.toDrive(**export_params)
task.start()
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
task.status()
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>






    {'state': 'READY',
     'description': 'Sentinel_AC',
     'creation_timestamp_ms': 1700793382708,
     'update_timestamp_ms': 1700793382708,
     'start_timestamp_ms': 0,
     'task_type': 'EXPORT_IMAGE',
     'id': 'AFK6RUHAX4YNYT4G4K4SGOST',
     'name': 'projects/earthengine-legacy/operations/AFK6RUHAX4YNYT4G4K4SGOST'}



**EXPORT TO GOOGLE EARTH ENGINE**


```python
# # set some properties for export
dateString = scene_date.strftime("%Y-%m-%d")
ref = ref.set({'satellite':'Sentinel 2',
              'fileID':info['system:index'],
              'date':dateString,
              'aerosol_optical_thickness':aot,
              'water_vapour':h2o,
              'ozone':o3})
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Define YOUR Google Earth Engine assetID
# in my case it was something like this..
assetID = 'users/Hareeshrao-LC60/Atmospheric_Correction' +dateString
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
# Define the region using a polygon or coordinates
region = ee.Geometry.Polygon(
    [[
        [130.9825040586519, -12.482652274143653],
        [130.9825040586519, -12.591236530819916],
        [130.80603616314409, -12.591236530819916],
        [130.80603616314409, -12.482652274143653]
    ]])

# Export
export = ee.batch.Export.image.toAsset(\
    image=ref,
    description='sentinel2_atmcorr_export',
    assetId = assetID,
    region = region)

# uncomment to run the export
export.start()
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



# **Extract Pixel Values**


```python
import rasterio
import pandas as pd

# Replace 'your_exported_image.tif' with the actual filename
tiff_file_path = 'C:/Users/haree/Desktop/Methane/Sentinel_AC.tif'

# Open the GeoTIFF file using rasterio
with rasterio.open(tiff_file_path) as src:
    # Read the entire image as a NumPy array
    image_array = src.read()
    
    # Get spatial information
    transform = src.transform
    metadata = src.meta

# Get image dimensions (rows, columns, bands)
rows, cols, bands = image_array.shape

# Reshape the array for easy conversion to DataFrame
reshaped_array = image_array.reshape((rows * cols, bands))

# Create a DataFrame from the reshaped array
df = pd.DataFrame(reshaped_array, columns=[f'Band_{i+1}' for i in range(bands)])

# Add latitude and longitude columns
df['Latitude'], df['Longitude'] = zip(*[transform * (col, row) for row in range(rows) for col in range(cols)])

# Display the array (for demonstration purposes)
print("Pixel Values:")
print(image_array)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



    Pixel Values:
    [[[   0    0    0 ... 3058 3058 2782]
      [   0    0    0 ... 2556 2556 2270]
      [   0    0    0 ... 2556 2556 2270]
      ...
      [   0    0    0 ... 2484 2484 2144]
      [   0    0    0 ... 2484 2484 2144]
      [   0    0    0 ... 2364 2364 2542]]
    
     [[   0    0    0 ... 2255 2255 2279]
      [   0    0    0 ... 1834 1834 1478]
      [   0    0    0 ... 1834 1834 1478]
      ...
      [   0    0    0 ... 1383 1383 1280]
      [   0    0    0 ... 1383 1383 1280]
      [   0    0    0 ... 1304 1304 1440]]]
    


```python
# Export DataFrame to CSV
csv_file_path = 'pixel_values.csv'
df.to_csv(csv_file_path, index=True)

print(f"CSV file '{csv_file_path}' exported successfully.")
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



    CSV file 'pixel_values.csv' exported successfully.
    

# **Plot Pixel Values Graph**


```python
with rasterio.open(tiff_file_path) as src:
    # Get metadata
    metadata = src.meta

    # Get CRS
    crs = src.crs

print("Metadata:", metadata)
print("CRS:", crs)

```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



    Metadata: {'driver': 'GTiff', 'dtype': 'uint16', 'nodata': None, 'width': 1928, 'height': 1216, 'count': 2, 'crs': CRS.from_epsg(32752), 'transform': Affine(10.0, 0.0, 696190.0,
           0.0, -10.0, 8619410.0)}
    CRS: EPSG:32752
    


```python
from affine import Affine

# Extracted from your metadata
transform = Affine(10.0, 0.0, 696190.0, 0.0, -10.0, 8619410.0)

# Calculate the center coordinates of the pixel at row i, column j
i = 500  # Replace with your desired row index
j = 800  # Replace with your desired column index

x = transform[0] + j * transform[1] + i * transform[2]
y = transform[3] + j * transform[4] + i * transform[5]

print("X coordinate:", x)
print("Y coordinate:", y)

```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



    X coordinate: 348095010.0
    Y coordinate: 4309697000.0
    


```python
# Install modules
!pip install pyproj
!pip install pyepsg

# Transform CRS to Lon, Lat
from pyproj import CRS, Transformer

source_crs = CRS.from_epsg(32752)
target_crs = CRS.from_epsg(4326) #Based on World Geodetic System (WGS84)

transformer = Transformer.from_crs(source_crs, target_crs)

#Define x and y
x = 348095010.0
y = 4309697000.0

lon, lat = transformer.transform(x, y)

# Print the transformed coordinates
print("Longitude:", lon)
print("Latitude:", lat)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



    Requirement already satisfied: pyproj in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (3.6.1)
    Requirement already satisfied: certifi in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from pyproj) (2023.7.22)
    Requirement already satisfied: pyepsg in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (0.4.0)
    Requirement already satisfied: requests in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from pyepsg) (2.31.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from requests->pyepsg) (2.0.4)
    Requirement already satisfied: idna<4,>=2.5 in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from requests->pyepsg) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from requests->pyepsg) (1.26.18)
    Requirement already satisfied: certifi>=2017.4.17 in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from requests->pyepsg) (2023.7.22)
    Longitude: inf
    Latitude: inf
    


```python

import rioxarray

# Replace 'your_exported_image.tif' with the actual filename
tiff_file_path = 'C:/Users/haree/Desktop/Methane/Sentinel_AC.tif'
rds = rioxarray.open_rasterio(tiff_file_path)
rds_4326 = rds.rio.reproject("EPSG:4326")
rds_4326.rio.to_raster("file.tif")

rds_4326.rio.to_raster("file.tif", compress="DEFLATE", tiled=True)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




```python
import ee
import geemap
import folium


# Function to mask clouds using the Sentinel-2 QA band

# Function to calculate methane concentration from Sentinel-2 image
def calculate_methane_concentration(image):
    # Replace 'your_band_name' with the actual band containing atmospheric correction results
    methane_band = image.select('B12')
    # Specify the conversion factor if needed
    # methane_concentration = methane_band.multiply(CONVERSION_FACTOR)
    return methane_band

# Replace 'your_sentinel_image' with the actual Sentinel image
sentinel_image = ee.Image(S2_TOA)

# Apply atmospheric correction if needed
#atmospheric_corrected_image = sentinel_image.some_atmospheric_correction_function()

# Mask clouds
#masked_image = mask_clouds(atmospheric_corrected_image)

# Calculate methane concentration
methane_concentration_image = calculate_methane_concentration(sentinel_image)

# Display the methane concentration on the Folium map
Map = geemap.Map()
Map.centerObject(methane_concentration_image, zoom=10)
Map.addLayer(methane_concentration_image, {
    'bands': ['B12'],
    'min': 0,
    'max': 200  # Adjust the min and max values as needed
}, 'Methane Concentration')
Map.addLayerControl()
Map

# You can now visualize the methane concentration on the Folium map and further analyze the data.

```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>






    Map(center=[-12.235938770667586, 131.32795419893583], controls=(WidgetControl(options=['position', 'transparen…




```python
import ee
import geemap
import folium


# Function to mask clouds using the Sentinel-2 QA band

# Function to calculate methane concentration from Sentinel-2 image
def calculate_methane_concentration(image):
    # Replace 'your_band_name' with the actual band containing atmospheric correction results
    methane_band = image.select('B8')
    # Specify the conversion factor if needed
    # methane_concentration = methane_band.multiply(CONVERSION_FACTOR)
    return methane_band

# Replace 'your_sentinel_image' with the actual Sentinel image
sentinel_image = ee.Image(S2_TOA)

# Apply atmospheric correction if needed
#atmospheric_corrected_image = sentinel_image.some_atmospheric_correction_function()

# Mask clouds
#masked_image = mask_clouds(atmospheric_corrected_image)

# Calculate methane concentration
methane_concentration_image = calculate_methane_concentration(sentinel_image)

# Display the methane concentration on the Folium map
Map = geemap.Map()
Map.centerObject(methane_concentration_image, zoom=10)
Map.addLayer(methane_concentration_image, {
    'bands': ['B8'],
    'min': 0,
    'max': 200  # Adjust the min and max values as needed
}, 'Methane Concentration')
Map.addLayerControl()
Map

# You can now visualize the methane concentration on the Folium map and further analyze the data.

```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>






    Map(center=[-12.235938770667586, 131.32795419893583], controls=(WidgetControl(options=['position', 'transparen…



# **Plume Transmission Ratio**


```python
S2_AC_asset_id = 'users/Hareeshrao-LC60/Atmospheric_Correction2023-09-01'
S2_AC = ee.Image(S2_AC_asset_id)

display(S2_AC)
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<div><style>:root {
  --font-color-primary: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --font-color-secondary: var(--jp-content-font-color2, rgba(0, 0, 0, 0.6));
  --font-color-accent: rgba(123, 31, 162, 1);
  --border-color: var(--jp-border-color2, #e0e0e0);
  --background-color: var(--jp-layout-color0, white);
  --background-color-row-even: var(--jp-layout-color1, white);
  --background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme="dark"],
body[data-theme="dark"],
body.vscode-dark {
  --font-color-primary: rgba(255, 255, 255, 1);
  --font-color-secondary: rgba(255, 255, 255, 0.6);
  --font-color-accent: rgb(173, 132, 190);
  --border-color: #2e2e2e;
  --background-color: #111111;
  --background-color-row-even: #111111;
  --background-color-row-odd: #313131;
}

.ee {
  padding: 1em;
  line-height: 1.5em;
  min-width: 300px;
  max-width: 1200px;
  overflow-y: scroll;
  max-height: 600px;
  border: 1px solid var(--border-color);
  font-family: monospace;
}

.ee li {
  list-style-type: none;
}

.ee ul {
  padding-left: 1.5em !important;
  margin: 0;
}

.ee > ul {
  padding-left: 0 !important;
}

.ee-open,
.ee-shut {
  color: var(--font-color-secondary);
  cursor: pointer;
  margin: 0;
}

.ee-open:hover,
.ee-shut:hover {
  color: var(--font-color-primary);
}

.ee-k {
  color: var(--font-color-accent);
  margin-right: 6px;
}

.ee-v {
  color: var(--font-color-primary);
}

.ee-toggle {
  display: none;
}

.ee-shut + ul {
  display: none;
}

.ee-open + ul {
  display: block;
}

.ee-shut::before {
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transform: rotate(-90deg);
  transition: transform 0.2s;
}

.ee-open::before {
  transform: rotate(0deg);
  display: inline-block;
  content: "▼";
  margin-right: 6px;
  transition: transform 0.2s;
}
</style><div class='ee'><ul><li><label class='ee-shut'>Image users/Hareeshrao-LC60/Atmospheric_Correction2023-09-01 (3 bands)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>Image</span></li><li><span class='ee-k'>id:</span><span class='ee-v'>users/Hareeshrao-LC60/Atmospheric_Correction2023-09-01</span></li><li><span class='ee-k'>version:</span><span class='ee-v'>1700713094529882</span></li><li><label class='ee-shut'>bands: List (3 elements)<input type='checkbox' class='ee-toggle'></label><ul><li><label class='ee-shut'>0: "B12", double, EPSG:32752, 776x607 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B12</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8619380]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8619380</span></li></ul></li><li><label class='ee-shut'>data_type: double<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>double</span></li></ul></li><li><label class='ee-shut'>dimensions: [776, 607]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>776</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>607</span></li></ul></li></ul></li><li><label class='ee-shut'>1: "B11", double, EPSG:32752, 776x607 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B11</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8619380]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8619380</span></li></ul></li><li><label class='ee-shut'>data_type: double<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>double</span></li></ul></li><li><label class='ee-shut'>dimensions: [776, 607]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>776</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>607</span></li></ul></li></ul></li><li><label class='ee-shut'>2: "B8", double, EPSG:32752, 776x607 px<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>id:</span><span class='ee-v'>B8</span></li><li><span class='ee-k'>crs:</span><span class='ee-v'>EPSG:32752</span></li><li><label class='ee-shut'>crs_transform: [20, 0, 699960, 0, -20, 8619380]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>20</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>2:</span><span class='ee-v'>699960</span></li><li><span class='ee-k'>3:</span><span class='ee-v'>0</span></li><li><span class='ee-k'>4:</span><span class='ee-v'>-20</span></li><li><span class='ee-k'>5:</span><span class='ee-v'>8619380</span></li></ul></li><li><label class='ee-shut'>data_type: double<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>PixelType</span></li><li><span class='ee-k'>precision:</span><span class='ee-v'>double</span></li></ul></li><li><label class='ee-shut'>dimensions: [776, 607]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>776</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>607</span></li></ul></li></ul></li></ul></li><li><label class='ee-shut'>properties: Object (8 properties)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>aerosol_optical_thickness:</span><span class='ee-v'>0.22833332419395447</span></li><li><span class='ee-k'>date:</span><span class='ee-v'>2023-09-01</span></li><li><span class='ee-k'>fileID:</span><span class='ee-v'>20230901T013701_20230901T013903_T52LGM</span></li><li><span class='ee-k'>ozone:</span><span class='ee-v'>0.274</span></li><li><span class='ee-k'>satellite:</span><span class='ee-v'>Sentinel 2</span></li><li><span class='ee-k'>system:asset_size:</span><span class='ee-v'>5790206</span></li><li><label class='ee-shut'>system:footprint: LinearRing (19 vertices)<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>type:</span><span class='ee-v'>LinearRing</span></li><li><label class='ee-shut'>coordinates: List (19 elements)<input type='checkbox' class='ee-toggle'></label><ul><li><label class='ee-shut'>0: [130.98259908716622, -12.481557929570444]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.98259908716622</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.481557929570444</span></li></ul></li><li><label class='ee-shut'>1: [130.98257598778272, -12.481556688788714]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.98257598778272</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.481556688788714</span></li></ul></li><li><label class='ee-shut'>2: [130.84001150202923, -12.482567068098714]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.84001150202923</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.482567068098714</span></li></ul></li><li><label class='ee-shut'>3: [130.83992705559896, -12.482640833561979]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.83992705559896</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.482640833561979</span></li></ul></li><li><label class='ee-shut'>4: [130.83983388649546, -12.48270367432374]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.83983388649546</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.48270367432374</span></li></ul></li><li><label class='ee-shut'>5: [130.83982832876453, -12.482733235917374]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.83982832876453</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.482733235917374</span></li></ul></li><li><label class='ee-shut'>6: [130.84060617428284, -12.592292988690453]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.84060617428284</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.592292988690453</span></li></ul></li><li><label class='ee-shut'>7: [130.84068166572425, -12.592375415581452]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.84068166572425</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.592375415581452</span></li></ul></li><li><label class='ee-shut'>8: [130.84074604178286, -12.592466434212096]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.84074604178286</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.592466434212096</span></li></ul></li><li><label class='ee-shut'>9: [130.84076873548415, -12.592470497471384]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.84076873548415</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.592470497471384</span></li></ul></li><li><label class='ee-shut'>10: [130.8407918151235, -12.592471744024367]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.8407918151235</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.592471744024367</span></li></ul></li><li><label class='ee-shut'>11: [130.98341672229992, -12.591452132836631]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.98341672229992</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.591452132836631</span></li></ul></li><li><label class='ee-shut'>12: [130.98350111075442, -12.591378408232035]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.98350111075442</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.591378408232035</span></li></ul></li><li><label class='ee-shut'>13: [130.98359427669467, -12.591315501970044]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.98359427669467</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.591315501970044</span></li></ul></li><li><label class='ee-shut'>14: [130.98359982044832, -12.591285941244402]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.98359982044832</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.591285941244402</span></li></ul></li><li><label class='ee-shut'>15: [130.9827617065606, -12.481735340668179]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.9827617065606</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.481735340668179</span></li></ul></li><li><label class='ee-shut'>16: [130.9826861717577, -12.481652947250295]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.9826861717577</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.481652947250295</span></li></ul></li><li><label class='ee-shut'>17: [130.98262172455298, -12.481561992744101]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.98262172455298</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.481561992744101</span></li></ul></li><li><label class='ee-shut'>18: [130.98259908716622, -12.481557929570444]<input type='checkbox' class='ee-toggle'></label><ul><li><span class='ee-k'>0:</span><span class='ee-v'>130.98259908716622</span></li><li><span class='ee-k'>1:</span><span class='ee-v'>-12.481557929570444</span></li></ul></li></ul></li></ul></li><li><span class='ee-k'>water_vapour:</span><span class='ee-v'>1.8299999237060547</span></li></ul></li></ul></li></ul></div><script>function toggleHeader() {
    const parent = this.parentElement;
    parent.className = parent.className === "ee-open" ? "ee-shut" : "ee-open";
}

for (let c of document.getElementsByClassName("ee-toggle")) {
    c.onclick = toggleHeader;
}</script></div>



```python
# Function to calculate methane concentration from Sentinel-2 image
def calculate_methane_enhancement(S2_TOA):
    # Replace 'your_band_name' with the actual band containing atmospheric correction results
    methane_band =S2_TOA.select('B12')
    methane_free_band =S2_TOA.select('B11')
    scale=S2_TOA.projection().nominalScale(),
                        
    # Calculate the ratio of methane band to methane-free band
    methane_ratio = methane_band.divide(methane_free_band)
    
    # Calculate methane enhancement
    methane_enhancement = methane_ratio.subtract(1)
    
    return methane_enhancement
    # Specify the conversion factor if needed
    # methane_concentration = methane_band.multiply(CONVERSION_FACTOR)
    return methane_band

# Replace 'your_sentinel_image' with the actual Sentinel image
sentinel_image = ee.Image(S2_AC)

# Apply atmospheric correction if needed
# atmospheric_corrected_image = sentinel_image.some_atmospheric_correction_function() 

# Mask clouds
#masked_image = mask_clouds(atmospheric_corrected_image)

# Calculate methane enhancement
methane_enhancement_image = calculate_methane_enhancement(sentinel_image)

# Display the methane enhancement on the Folium map
Map = geemap.Map()
Map.centerObject(methane_enhancement_image, zoom=10)
Map.addLayer(methane_enhancement_image, {
    'min': 0.5,
    'max': 0.7,
    'palette': ['purple', 'white', 'red']  # Adjust the palette as needed
}, 'Methane Enhancement')
Map.addLayerControl()
Map
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>






    Map(center=[-12.537021337810492, 130.9116975318995], controls=(WidgetControl(options=['position', 'transparent…



# **Add Scaling Factor**


```python
import ee
import numpy as np
from sklearn.linear_model import LinearRegression

# Initialize Google Earth Engine
ee.Initialize()

# Replace 'methane_band_name' and 'methane_free_band_name' with the actual band names
methane_band_name = 'B12'
methane_free_band_name = 'B11'

# Load the atmospherically corrected Sentinel-2 image
S2_ME = ee.Image(S2_AC)

# Select the methane and methane-free bands
methane_band = S2_ME.select(methane_band_name)
methane_free_band = S2_ME.select(methane_free_band_name)

# Get the data as NumPy arrays
methane_data = np.array(methane_band.reduceRegion(reducer=ee.Reducer.toList(), geometry=S2_ME.geometry(), scale=10).get(methane_band_name).getInfo())
methane_free_data = np.array(methane_free_band.reduceRegion(reducer=ee.Reducer.toList(), geometry=S2_ME.geometry(), scale=10).get(methane_free_band_name).getInfo())

# Reshape the data for scikit-learn
X = methane_free_data.reshape(-1, 1)
y = methane_data.reshape(-1, 1)

# Fit a linear regression model
model = LinearRegression().fit(X, y)

# Extract the scaling factor 'c'
scaling_factor_c = model.coef_[0][0]

display(model)
print("Scaling Factor (c):", scaling_factor_c)

```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>


    Scaling Factor (c): 0.011597993134691575
    


```python
import ee
import folium
import geemap

# Initialize Google Earth Engine
ee.Initialize()

# Replace 'methane_band_name' and 'methane_free_band_name' with the actual band names
methane_band_name = 'B12'
methane_free_band_name = 'B11'

# Load the atmospherically corrected Sentinel-2 image
S2_ME = ee.Image(S2_AC)

# Select the methane and methane-free bands
methane_band = S2_ME.select(methane_band_name)
methane_free_band = S2_ME.select(methane_free_band_name)

# Calculate Methane Enhancement (ME) using the scaling factor
methane_ratio = methane_band.divide(methane_free_band)
                 
methane_minus = methane_ratio.subtract(1)

#methane_enhancement = methane_minus.multiply(scaling_factor_c)

# Display the Methane Enhancement on the Folium map
Map = geemap.Map()
Map.centerObject(S2_ME, zoom=12)

# Add layers to the Folium map
Map.add_ee_layer(methane_minus, {
    'min': 0.1,
    'max': 0.3,  # Adjust the min and max values as needed
    'palette': ['purple', 'white', 'red']
}, 'Methane Enhancement')

# Add layer control panel to the map
Map.addLayerControl()

# Display the map
display(Map)

```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>




    Map(center=[-12.537021286275174, 130.91169810323842], controls=(WidgetControl(options=['position', 'transparen…



```python
!pip install scikit-learn
```



<style>
    .geemap-dark {
        --jp-widgets-color: white;
        --jp-widgets-label-color: white;
        --jp-ui-font-color1: white;
        --jp-layout-color2: #454545;
        background-color: #383838;
    }

    .geemap-dark .jupyter-button {
        --jp-layout-color3: #383838;
    }

    .geemap-colab {
        background-color: var(--colab-primary-surface-color, white);
    }

    .geemap-colab .jupyter-button {
        --jp-layout-color3: var(--colab-primary-surface-color, white);
    }
</style>



    Requirement already satisfied: scikit-learn in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (1.3.2)
    Requirement already satisfied: numpy<2.0,>=1.17.3 in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from scikit-learn) (1.26.0)
    Requirement already satisfied: scipy>=1.5.0 in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from scikit-learn) (1.11.3)
    Requirement already satisfied: joblib>=1.1.1 in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from scikit-learn) (1.3.2)
    Requirement already satisfied: threadpoolctl>=2.0.0 in d:\programsdata\anaconda\envs\methane_ac\lib\site-packages (from scikit-learn) (3.2.0)
    


```python

```
