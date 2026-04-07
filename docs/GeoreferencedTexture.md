

# Class: GeoreferencedTexture 


_A GeoreferencedTexture is a texture that uses a planimetric projection. It contains an implicit parameterization that is either stored within the image file, an accompanying world file or specified using the orientation and referencePoint elements._





URI: [citygml:GeoreferencedTexture](https://www.ogc.org/standards/citygml/GeoreferencedTexture)





```mermaid
 classDiagram
    class GeoreferencedTexture
    click GeoreferencedTexture href "../GeoreferencedTexture/"
      AbstractTexture <|-- GeoreferencedTexture
        click AbstractTexture href "../AbstractTexture/"
      
      GeoreferencedTexture : adeOfAbstractFeature
        
          
    
        
        
        GeoreferencedTexture --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      GeoreferencedTexture : adeOfAbstractSurfaceData
        
          
    
        
        
        GeoreferencedTexture --> "*" ADEOfAbstractSurfaceData : adeOfAbstractSurfaceData
        click ADEOfAbstractSurfaceData href "../ADEOfAbstractSurfaceData/"
    

        
      GeoreferencedTexture : adeOfAbstractTexture
        
          
    
        
        
        GeoreferencedTexture --> "*" ADEOfAbstractTexture : adeOfAbstractTexture
        click ADEOfAbstractTexture href "../ADEOfAbstractTexture/"
    

        
      GeoreferencedTexture : adeOfGeoreferencedTexture
        
          
    
        
        
        GeoreferencedTexture --> "*" ADEOfGeoreferencedTexture : adeOfGeoreferencedTexture
        click ADEOfGeoreferencedTexture href "../ADEOfGeoreferencedTexture/"
    

        
      GeoreferencedTexture : borderColor
        
          
    
        
        
        GeoreferencedTexture --> "0..1" ColorPlusOpacity : borderColor
        click ColorPlusOpacity href "../ColorPlusOpacity/"
    

        
      GeoreferencedTexture : description
        
      GeoreferencedTexture : featureID
        
          
    
        
        
        GeoreferencedTexture --> "1" ID : featureID
        click ID href "../ID/"
    

        
      GeoreferencedTexture : identifier
        
      GeoreferencedTexture : imageURI
        
      GeoreferencedTexture : isFront
        
      GeoreferencedTexture : mimeType
        
          
    
        
        
        GeoreferencedTexture --> "0..1" MimeTypeValue : mimeType
        click MimeTypeValue href "../MimeTypeValue/"
    

        
      GeoreferencedTexture : name
        
      GeoreferencedTexture : orientation
        
          
    
        
        
        GeoreferencedTexture --> "0..1" TransformationMatrix2x2 : orientation
        click TransformationMatrix2x2 href "../TransformationMatrix2x2/"
    

        
      GeoreferencedTexture : preferWorldFile
        
      GeoreferencedTexture : referencePoint
        
      GeoreferencedTexture : target
        
      GeoreferencedTexture : textureType
        
          
    
        
        
        GeoreferencedTexture --> "0..1" TextureType : textureType
        click TextureType href "../TextureType/"
    

        
      GeoreferencedTexture : wrapMode
        
          
    
        
        
        GeoreferencedTexture --> "0..1" WrapMode : wrapMode
        click WrapMode href "../WrapMode/"
    

        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractSurfaceData](AbstractSurfaceData.md)
        * [AbstractTexture](AbstractTexture.md)
            * **GeoreferencedTexture**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [preferWorldFile](preferWorldFile.md) | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the georeference from the image file or the accompanying wo... | direct |
| [orientation](orientation.md) | 0..1 <br/> [TransformationMatrix2x2](TransformationMatrix2x2.md) | Specifies the rotation and scaling of the image in form of a 2x2 matrix | direct |
| [target](target.md) | * <br/> [Uri](Uri.md) | Specifies the URI that points to the surface geometry objects to which the te... | direct |
| [adeOfGeoreferencedTexture](adeOfGeoreferencedTexture.md) | * <br/> [ADEOfGeoreferencedTexture](ADEOfGeoreferencedTexture.md) | Augments the GeoreferencedTexture with properties defined in an ADE | direct |
| [referencePoint](referencePoint.md) | 0..1 <br/> [String](String.md) | Relates to the 2D Point geometry that represents the center of the upper left... | direct |
| [imageURI](imageURI.md) | 1 <br/> [Uri](Uri.md) | Specifies the URI that points to the external image data file | [AbstractTexture](AbstractTexture.md) |
| [mimeType](mimeType.md) | 0..1 <br/> [MimeTypeValue](MimeTypeValue.md) | Specifies the MIME type of the external point cloud file | [AbstractTexture](AbstractTexture.md) |
| [textureType](textureType.md) | 0..1 <br/> [TextureType](TextureType.md) | Indicates the specific type of the texture | [AbstractTexture](AbstractTexture.md) |
| [wrapMode](wrapMode.md) | 0..1 <br/> [WrapMode](WrapMode.md) | Specifies the behaviour of the texture when the texture is smaller than the s... | [AbstractTexture](AbstractTexture.md) |
| [borderColor](borderColor.md) | 0..1 <br/> [ColorPlusOpacity](ColorPlusOpacity.md) | Specifies the color of that part of the surface that is not covered by the te... | [AbstractTexture](AbstractTexture.md) |
| [adeOfAbstractTexture](adeOfAbstractTexture.md) | * <br/> [ADEOfAbstractTexture](ADEOfAbstractTexture.md) | Augments AbstractTexture with properties defined in an ADE | [AbstractTexture](AbstractTexture.md) |
| [isFront](isFront.md) | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the texture or material is assigned to the front side or th... | [AbstractSurfaceData](AbstractSurfaceData.md) |
| [adeOfAbstractSurfaceData](adeOfAbstractSurfaceData.md) | * <br/> [ADEOfAbstractSurfaceData](ADEOfAbstractSurfaceData.md) | Augments AbstractSurfaceData with properties defined in an ADE | [AbstractSurfaceData](AbstractSurfaceData.md) |
| [featureID](featureID.md) | 1 <br/> [ID](ID.md) |  | [AbstractFeature](AbstractFeature.md) |
| [identifier](identifier.md) | 0..1 <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [name](name.md) | * <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AbstractFeature](AbstractFeature.md) |
| [adeOfAbstractFeature](adeOfAbstractFeature.md) | * <br/> [ADEOfAbstractFeature](ADEOfAbstractFeature.md) | Augments AbstractFeature with properties defined in an ADE | [AbstractFeature](AbstractFeature.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.ogc.org/standards/citygml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | citygml:GeoreferencedTexture |
| native | citygml:GeoreferencedTexture |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeoreferencedTexture
description: A GeoreferencedTexture is a texture that uses a planimetric projection.
  It contains an implicit parameterization that is either stored within the image
  file, an accompanying world file or specified using the orientation and referencePoint
  elements.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTexture
abstract: false
attributes:
  preferWorldFile:
    name: preferWorldFile
    description: Indicates whether the georeference from the image file or the accompanying
      world file should be preferred.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - GeoreferencedTexture
    range: boolean
    required: false
    multivalued: false
  orientation:
    name: orientation
    description: Specifies the rotation and scaling of the image in form of a 2x2
      matrix.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - GeoreferencedTexture
    range: TransformationMatrix2x2
    required: false
    multivalued: false
  target:
    name: target
    description: Specifies the URI that points to the surface geometry objects to
      which the texture is applied.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - GeoreferencedTexture
    - X3DMaterial
    range: uri
    required: false
    multivalued: true
  adeOfGeoreferencedTexture:
    name: adeOfGeoreferencedTexture
    description: Augments the GeoreferencedTexture with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - GeoreferencedTexture
    range: ADEOfGeoreferencedTexture
    required: false
    multivalued: true
  referencePoint:
    name: referencePoint
    description: Relates to the 2D Point geometry that represents the center of the
      upper left image pixel in world space.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - GeoreferencedTexture
    - ImplicitGeometry
    range: string
    required: false
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: GeoreferencedTexture
description: A GeoreferencedTexture is a texture that uses a planimetric projection.
  It contains an implicit parameterization that is either stored within the image
  file, an accompanying world file or specified using the orientation and referencePoint
  elements.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractTexture
abstract: false
attributes:
  preferWorldFile:
    name: preferWorldFile
    description: Indicates whether the georeference from the image file or the accompanying
      world file should be preferred.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: preferWorldFile
    owner: GeoreferencedTexture
    domain_of:
    - GeoreferencedTexture
    range: boolean
    required: false
    multivalued: false
  orientation:
    name: orientation
    description: Specifies the rotation and scaling of the image in form of a 2x2
      matrix.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: orientation
    owner: GeoreferencedTexture
    domain_of:
    - GeoreferencedTexture
    range: TransformationMatrix2x2
    required: false
    multivalued: false
  target:
    name: target
    description: Specifies the URI that points to the surface geometry objects to
      which the texture is applied.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: target
    owner: GeoreferencedTexture
    domain_of:
    - GeoreferencedTexture
    - X3DMaterial
    range: uri
    required: false
    multivalued: true
  adeOfGeoreferencedTexture:
    name: adeOfGeoreferencedTexture
    description: Augments the GeoreferencedTexture with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfGeoreferencedTexture
    owner: GeoreferencedTexture
    domain_of:
    - GeoreferencedTexture
    range: ADEOfGeoreferencedTexture
    required: false
    multivalued: true
  referencePoint:
    name: referencePoint
    description: Relates to the 2D Point geometry that represents the center of the
      upper left image pixel in world space.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: referencePoint
    owner: GeoreferencedTexture
    domain_of:
    - GeoreferencedTexture
    - ImplicitGeometry
    range: string
    required: false
    multivalued: false
  imageURI:
    name: imageURI
    description: Specifies the URI that points to the external image data file.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: imageURI
    owner: GeoreferencedTexture
    domain_of:
    - AbstractTexture
    range: uri
    required: true
    multivalued: false
  mimeType:
    name: mimeType
    description: Specifies the MIME type of the external point cloud file.
    from_schema: https://www.ogc.org/standards/citygml
    alias: mimeType
    owner: GeoreferencedTexture
    domain_of:
    - StandardFileTimeseries
    - TabulatedFileTimeseries
    - PointCloud
    - AbstractTexture
    - ImplicitGeometry
    range: MimeTypeValue
    required: false
    multivalued: false
  textureType:
    name: textureType
    description: Indicates the specific type of the texture.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: textureType
    owner: GeoreferencedTexture
    domain_of:
    - AbstractTexture
    range: TextureType
    required: false
    multivalued: false
  wrapMode:
    name: wrapMode
    description: Specifies the behaviour of the texture when the texture is smaller
      than the surface to which it is applied.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: wrapMode
    owner: GeoreferencedTexture
    domain_of:
    - AbstractTexture
    range: WrapMode
    required: false
    multivalued: false
  borderColor:
    name: borderColor
    description: Specifies the color of that part of the surface that is not covered
      by the texture.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: borderColor
    owner: GeoreferencedTexture
    domain_of:
    - AbstractTexture
    range: ColorPlusOpacity
    required: false
    multivalued: false
  adeOfAbstractTexture:
    name: adeOfAbstractTexture
    description: Augments AbstractTexture with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractTexture
    owner: GeoreferencedTexture
    domain_of:
    - AbstractTexture
    range: ADEOfAbstractTexture
    required: false
    multivalued: true
  isFront:
    name: isFront
    description: Indicates whether the texture or material is assigned to the front
      side or the back side of the surface geometry object.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: isFront
    owner: GeoreferencedTexture
    domain_of:
    - AbstractSurfaceData
    range: boolean
    required: false
    multivalued: false
  adeOfAbstractSurfaceData:
    name: adeOfAbstractSurfaceData
    description: Augments AbstractSurfaceData with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractSurfaceData
    owner: GeoreferencedTexture
    domain_of:
    - AbstractSurfaceData
    range: ADEOfAbstractSurfaceData
    required: false
    multivalued: true
  featureID:
    name: featureID
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: featureID
    owner: GeoreferencedTexture
    domain_of:
    - AbstractFeature
    range: ID
    required: true
    multivalued: false
  identifier:
    name: identifier
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: identifier
    owner: GeoreferencedTexture
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: GeoreferencedTexture
    domain_of:
    - CodeAttribute
    - DateAttribute
    - DoubleAttribute
    - GenericAttributeSet
    - IntAttribute
    - MeasureAttribute
    - StringAttribute
    - UriAttribute
    - AbstractFeature
    range: string
    required: false
    multivalued: true
  description:
    name: description
    from_schema: https://www.ogc.org/standards/citygml
    alias: description
    owner: GeoreferencedTexture
    domain_of:
    - ConstructionEvent
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  adeOfAbstractFeature:
    name: adeOfAbstractFeature
    description: Augments AbstractFeature with properties defined in an ADE.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: adeOfAbstractFeature
    owner: GeoreferencedTexture
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>