import 'dart:io';
import 'dart:typed_data';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Car state analysis',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  File? _imageFile;
  Uint8List? _imageBytes;
  String _analysisResult = 'No analysis yet.';

  Future<void> _pickImage() async {
    final ImagePicker picker = ImagePicker();
    final XFile? pickedFile = await picker.pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      if (kIsWeb) {
        _imageBytes = await pickedFile.readAsBytes();
        setState(() {
          _imageFile = null;
        });
      } else {
        setState(() {
          _imageFile = File(pickedFile.path);
          _imageBytes = null;
        });
      }
    } else {
      print('No image selected.');
    }
  }

  Future<void> _analyzeImage() async {
    if (_imageFile == null && _imageBytes == null) {
      setState(() {
        _analysisResult = 'Please select an image first.';
      });
      return;
    }

    final url = Uri.parse('http://localhost:8000/upload/'); // Correct endpoint

    try {
      var request = http.MultipartRequest('POST', url);

      if (_imageFile != null) {
        request.files.add(await http.MultipartFile.fromPath('file', _imageFile!.path));
      } else if (_imageBytes != null) {
        List<int> bytes = _imageBytes!.cast<int>();
        request.files.add(http.MultipartFile.fromBytes('file', bytes, filename: 'image.jpg'));
      }

      var response = await request.send();
      var responseBody = await response.stream.bytesToString();

      if (response.statusCode == 200) {
        final decodedResponse = jsonDecode(responseBody);
        setState(() {
          _analysisResult = decodedResponse['analytics'].toString(); // Access 'analytics'
        });
      } else {
        setState(() {
          _analysisResult = 'Error analyzing image: ${response.statusCode}';
        });
      }
    } catch (e) {
      setState(() {
        _analysisResult = 'Error: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Image Analysis App'),
      ),
      body: Row(
        children: [
          // Image Viewer
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: _imageFile == null && _imageBytes == null
                  ? const Center(child: Text('No image selected'))
                  : kIsWeb
                      ? Image.memory(
                          _imageBytes!,
                          fit: BoxFit.contain,
                        )
                      : Image.file(
                          _imageFile!,
                          fit: BoxFit.contain,
                        ),
            ),
          ),
          // Buttons
          Expanded(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: _pickImage,
                  child: const Text('Upload Image'),
                ),
                const SizedBox(height: 20),
                ElevatedButton(
                  onPressed: _analyzeImage,
                  child: const Text('Analyze'),
                ),
              ],
            ),
          ),
          // Analysis Result
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text(
                _analysisResult,
                style: const TextStyle(fontSize: 16),
              ),
            ),
          ),
        ],
      ),
    );
  }
}