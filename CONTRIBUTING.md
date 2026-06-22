# Contributing to Face Behavior Analysis

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 Ways to Contribute

- 🐛 **Report bugs** - Help us identify and fix issues
- ✨ **Suggest features** - Share your ideas for improvements
- 📝 **Improve documentation** - Make it clearer and more comprehensive
- 🔧 **Submit code** - Fix bugs or implement new features
- 🧪 **Write tests** - Improve test coverage
- 🎨 **Design improvements** - UI/UX enhancements

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/face-behavior-analysis.git
cd face-behavior-analysis
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## 📋 Development Guidelines

### Code Style

We follow [PEP 8](https://pep8.org/) style guide:

- Use **4 spaces** for indentation (no tabs)
- Maximum line length: **88 characters** (Black default)
- Use **descriptive variable names**
- Add **docstrings** to all functions and classes

```python
def detect_faces(image: np.ndarray, confidence: float = 0.9) -> List[Face]:
    """
    Detect faces in an image.
    
    Args:
        image: Input image as numpy array
        confidence: Minimum detection confidence (0.0-1.0)
    
    Returns:
        List of detected Face objects
    
    Raises:
        ValueError: If confidence is not in valid range
    
    Example:
        >>> image = cv2.imread('face.jpg')
        >>> faces = detect_faces(image, confidence=0.95)
        >>> print(f"Found {len(faces)} faces")
    """
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("Confidence must be between 0.0 and 1.0")
    
    # Implementation here
    return faces
```

### Code Formatting

We use automated tools:

```bash
# Format code with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Lint with flake8
flake8 src/ tests/

# Type check with mypy
mypy src/
```

### Testing

All new features must include tests:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_detector.py

# Run specific test
pytest tests/test_detector.py::test_face_detection
```

Example test:

```python
import pytest
from face_behavior import FaceAnalyzer

def test_face_detection():
    """Test basic face detection."""
    analyzer = FaceAnalyzer()
    
    # Load test image
    image = load_test_image('single_face.jpg')
    
    # Detect faces
    faces = analyzer.detect_faces(image)
    
    # Assert
    assert len(faces) == 1
    assert faces[0].confidence > 0.9

def test_invalid_input():
    """Test error handling for invalid input."""
    analyzer = FaceAnalyzer()
    
    with pytest.raises(ValueError):
        analyzer.detect_faces(None)
```

### Documentation

- Add docstrings to all public functions and classes
- Update README.md if adding new features
- Add examples to `examples/` directory
- Update CHANGELOG.md

## 🔄 Pull Request Process

### 1. Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No merge conflicts

### 2. Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
feat: add emotion detection for multiple faces
fix: correct bounding box coordinates in detection
docs: update API documentation for FaceAnalyzer
test: add integration tests for video processing
refactor: optimize face detection pipeline
perf: improve inference speed by 30%
chore: update dependencies to latest versions
```

Examples:
```bash
git commit -m "feat: add support for RetinaFace detector"
git commit -m "fix: resolve memory leak in video processing"
git commit -m "docs: add example for batch processing"
```

### 3. Pull Request Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Changes Made
- List key changes
- And their impact

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots showing the changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
```

### 4. Review Process

1. **Automated checks** - CI/CD must pass
2. **Code review** - At least one maintainer approval
3. **Testing** - Verify functionality
4. **Merge** - Squash and merge to main

## 🐛 Reporting Bugs

### Before Reporting

- Search existing issues
- Check if it's already fixed in latest version
- Gather relevant information

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Ubuntu 20.04]
- Python version: [e.g., 3.9.7]
- Package version: [e.g., 1.2.3]
- GPU: [e.g., NVIDIA RTX 3090]

## Additional Context
Screenshots, logs, etc.
```

## ✨ Feature Requests

### Feature Request Template

```markdown
## Feature Description
Clear description of the proposed feature

## Use Case
Why is this feature needed?

## Proposed Implementation
How could this be implemented?

## Alternatives Considered
Other approaches you've thought about

## Additional Context
Any other relevant information
```

## 📚 Documentation

### Documentation Standards

- Use clear, concise language
- Include code examples
- Add visual aids (diagrams, screenshots)
- Keep it up-to-date

### Building Documentation

```bash
# Install doc dependencies
pip install sphinx sphinx-rtd-theme

# Build docs
cd docs
make html

# View docs
open _build/html/index.html
```

## 🏆 Recognition

Contributors are recognized in:
- README.md Contributors section
- Release notes
- GitHub contributors page

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

**Positive behavior:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

**Unacceptable behavior:**
- Harassment of any kind
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information

### Enforcement

Report issues to: kiwios.cn@gmail.com

## 💬 Communication

- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - General questions and ideas
- **Pull Requests** - Code contributions
- **Email** - Private concerns

## 🎓 Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Git Workflow](https://guides.github.com/introduction/flow/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)

## ❓ Questions?

If you have questions, feel free to:
- Open a GitHub Discussion
- Comment on relevant issues
- Email the maintainers

---

**Thank you for contributing! 🎉**
