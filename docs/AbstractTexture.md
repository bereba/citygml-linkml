

# Class: AbstractTexture 


_AbstractTexture is the abstract superclass to represent the common attributes of the classes ParameterizedTexture and GeoreferencedTexture._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [citygml:AbstractTexture](https://www.ogc.org/standards/citygml/AbstractTexture)





```mermaid
 classDiagram
    class AbstractTexture
    click AbstractTexture href "../AbstractTexture/"
      AbstractSurfaceData <|-- AbstractTexture
        click AbstractSurfaceData href "../AbstractSurfaceData/"
      

      AbstractTexture <|-- GeoreferencedTexture
        click GeoreferencedTexture href "../GeoreferencedTexture/"
      AbstractTexture <|-- ParameterizedTexture
        click ParameterizedTexture href "../ParameterizedTexture/"
      

      AbstractTexture : adeOfAbstractFeature
        
          
    
        
        
        AbstractTexture --> "*" ADEOfAbstractFeature : adeOfAbstractFeature
        click ADEOfAbstractFeature href "../ADEOfAbstractFeature/"
    

        
      AbstractTexture : adeOfAbstractSurfaceData
        
          
    
        
        
        AbstractTexture --> "*" ADEOfAbstractSurfaceData : adeOfAbstractSurfaceData
        click ADEOfAbstractSurfaceData href "../ADEOfAbstractSurfaceData/"
    

        
      AbstractTexture : adeOfAbstractTexture
        
          
    
        
        
        AbstractTexture --> "*" ADEOfAbstractTexture : adeOfAbstractTexture
        click ADEOfAbstractTexture href "../ADEOfAbstractTexture/"
    

        
      AbstractTexture : borderColor
        
          
    
        
        
        AbstractTexture --> "0..1" ColorPlusOpacity : borderColor
        click ColorPlusOpacity href "../ColorPlusOpacity/"
    

        
      AbstractTexture : description
        
      AbstractTexture : featureID
        
          
    
        
        
        AbstractTexture --> "1" ID : featureID
        click ID href "../ID/"
    

        
      AbstractTexture : identifier
        
      AbstractTexture : imageURI
        
      AbstractTexture : isFront
        
      AbstractTexture : mimeType
        
          
    
        
        
        AbstractTexture --> "0..1" MimeTypeValue : mimeType
        click MimeTypeValue href "../MimeTypeValue/"
    

        
      AbstractTexture : name
        
      AbstractTexture : textureType
        
          
    
        
        
        AbstractTexture --> "0..1" TextureType : textureType
        click TextureType href "../TextureType/"
    

        
      AbstractTexture : wrapMode
        
          
    
        
        
        AbstractTexture --> "0..1" WrapMode : wrapMode
        click WrapMode href "../WrapMode/"
    

        
      
```





## Inheritance
* [AbstractFeature](AbstractFeature.md)
    * [AbstractSurfaceData](AbstractSurfaceData.md)
        * **AbstractTexture**
            * [GeoreferencedTexture](GeoreferencedTexture.md)
            * [ParameterizedTexture](ParameterizedTexture.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [imageURI](imageURI.md) | 1 <br/> [Uri](Uri.md) | Specifies the URI that points to the external image data file | direct |
| [mimeType](mimeType.md) | 0..1 <br/> [MimeTypeValue](MimeTypeValue.md) | Specifies the MIME type of the external point cloud file | direct |
| [textureType](textureType.md) | 0..1 <br/> [TextureType](TextureType.md) | Indicates the specific type of the texture | direct |
| [wrapMode](wrapMode.md) | 0..1 <br/> [WrapMode](WrapMode.md) | Specifies the behaviour of the texture when the texture is smaller than the s... | direct |
| [borderColor](borderColor.md) | 0..1 <br/> [ColorPlusOpacity](ColorPlusOpacity.md) | Specifies the color of that part of the surface that is not covered by the te... | direct |
| [adeOfAbstractTexture](adeOfAbstractTexture.md) | * <br/> [ADEOfAbstractTexture](ADEOfAbstractTexture.md) | Augments AbstractTexture with properties defined in an ADE | direct |
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
| self | citygml:AbstractTexture |
| native | citygml:AbstractTexture |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AbstractTexture
description: AbstractTexture is the abstract superclass to represent the common attributes
  of the classes ParameterizedTexture and GeoreferencedTexture.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractSurfaceData
abstract: true
attributes:
  imageURI:
    name: imageURI
    description: Specifies the URI that points to the external image data file.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    domain_of:
    - AbstractTexture
    range: uri
    required: true
    multivalued: false
  mimeType:
    name: mimeType
    description: Specifies the MIME type of the external point cloud file.
    from_schema: https://www.ogc.org/standards/citygml
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
    domain_of:
    - AbstractTexture
    range: ADEOfAbstractTexture
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: AbstractTexture
description: AbstractTexture is the abstract superclass to represent the common attributes
  of the classes ParameterizedTexture and GeoreferencedTexture.
from_schema: https://www.ogc.org/standards/citygml
is_a: AbstractSurfaceData
abstract: true
attributes:
  imageURI:
    name: imageURI
    description: Specifies the URI that points to the external image data file.
    from_schema: https://www.ogc.org/standards/citygml
    rank: 1000
    alias: imageURI
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
    domain_of:
    - AbstractFeature
    range: string
    required: false
    multivalued: false
  name:
    name: name
    from_schema: https://www.ogc.org/standards/citygml
    alias: name
    owner: AbstractTexture
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
    owner: AbstractTexture
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
    owner: AbstractTexture
    domain_of:
    - AbstractFeature
    range: ADEOfAbstractFeature
    required: false
    multivalued: true

```
</details>