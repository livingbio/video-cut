# Scene Generation

This package tries to generate scene list and the corresponding scene from input text

## INSTALLATION

You should have ffmpeg in your environment

usage:

```python
import generate_scenes
text_list = ['car', 'cat', 'dog']
filename = "example/1.mp4"
scene_list = generate_scenes.generate_scenes(text_list, filename)
```

The element in scene_list is as follows:

```python
{'result': [                                  # result contains a list of scene information
    {'duration': 13.412999999999997,          # duration: Duration of this scene
   'from_ts': 87.087,                         # from_ts: Start timestamp (in seconds)
   'image': 'frames/1.mp4.000006.jpg',        # image: Key image 
   'text': 'car',                             # text: Corresponding text
   'to_ts': 100.5},                           # to_ts: End timestamp (in seconds)
  {'duration': 17.951199999999996,
   'from_ts': 31.4648,
   'image': 'frames/1.mp4.000004.jpg',
   'text': 'cat',
   'to_ts': 49.416},
  {'duration': 7.307299999999998,
   'from_ts': 20.4871,
   'image': 'frames/1.mp4.000002.jpg',
   'text': 'dog',
   'to_ts': 27.7944}],
 'scene_list': [{'duration': 20.4871,          # scene_list contains all scene in the video 
   'from_ts': 0.0,
   'image': 'frames/1.mp4.000001.jpg',
   'to_ts': 20.4871},
  {'duration': 7.307299999999998,
   'from_ts': 20.4871,
   'image': 'frames/1.mp4.000002.jpg',
   'to_ts': 27.7944},
  {'duration': 3.6704000000000008,
   'from_ts': 27.7944,
   'image': 'frames/1.mp4.000003.jpg',
   'to_ts': 31.4648},
  {'duration': 17.951199999999996,
   'from_ts': 31.4648,
   'image': 'frames/1.mp4.000004.jpg',
   'to_ts': 49.416},
  {'duration': 37.67100000000001,
   'from_ts': 49.416,
   'image': 'frames/1.mp4.000005.jpg',
   'to_ts': 87.087},
  {'duration': 13.412999999999997,
   'from_ts': 87.087,
   'image': 'frames/1.mp4.000006.jpg',
   'to_ts': 100.5},
  {'duration': 7.707999999999998,
   'from_ts': 100.5,
   'image': 'frames/1.mp4.000007.jpg',
   'to_ts': 108.208},
  {'duration': 3.003,
   'from_ts': 108.208,
   'image': 'frames/1.mp4.000008.jpg',
   'to_ts': 111.211}]}
```

