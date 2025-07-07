<?php

namespace App\Controller;

use App\Entity\Institucion;
use App\Form\InstitucionType;
use App\Repository\InstitucionRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

use Symfony\Component\HttpFoundation\File\Exception\FileException;
use Symfony\Component\String\Slugger\SluggerInterface;

#[Route('/institucion')]
class InstitucionController extends AbstractController
{
    #[Route('/', name: 'app_institucion_index', methods: ['GET'])]
    public function index(InstitucionRepository $institucionRepository): Response
    {
        return $this->render('institucion/index.html.twig', [
            'institucions' => $institucionRepository->findAll(),
        ]);
    }

    #[Route('/new', name: 'app_institucion_new', methods: ['GET', 'POST'])]
    public function new(Request $request, EntityManagerInterface $entityManager): Response
    {
        $institucion = new Institucion();
        $form = $this->createForm(InstitucionType::class, $institucion);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $entityManager->persist($institucion);
            $entityManager->flush();

            $fotoFile = $form->get('foto')->getData();
            if ($fotoFile) {
                $nombreArchivo = $personal->getId() . '.' . $fotoFile->guessExtension();
                try {
                    $fotoFile->move(
                        $this->getParameter('fotos_institucion_dir'),
                        $nombreArchivo
                    );
                } catch (FileException $e) {
                    //  manejar error
                }
            }



            return $this->redirectToRoute('app_institucion_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->renderForm('institucion/new.html.twig', [
            'institucion' => $institucion,
            'form' => $form,
        ]);
    }

    #[Route('/{id}', name: 'app_institucion_show', methods: ['GET'])]
    public function show(Institucion $institucion): Response
    {
        return $this->render('institucion/show.html.twig', [
            'institucion' => $institucion,
        ]);
    }

    #[Route('/{id}/edit', name: 'app_institucion_edit', methods: ['GET', 'POST'])]
    public function edit(Request $request, Institucion $institucion, EntityManagerInterface $entityManager): Response
    {
        $form = $this->createForm(InstitucionType::class, $institucion);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $fotoFile = $form->get('foto')->getData();
            if ($fotoFile) {
                $nombreArchivo = $institucion->getId() . '.' . $fotoFile->guessExtension();
                try {
                    $fotoFile->move(
                        $this->getParameter('fotos_institucion_dir'),
                        $nombreArchivo
                    );
                } catch (FileException $e) {
                    // Opcional: manejar error
                }
            }


            $entityManager->flush();

            return $this->redirectToRoute('app_institucion_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->renderForm('institucion/edit.html.twig', [
            'institucion' => $institucion,
            'form' => $form,
        ]);
    }

    #[Route('/{id}', name: 'app_institucion_delete', methods: ['POST'])]
    public function delete(Request $request, Institucion $institucion, EntityManagerInterface $entityManager): Response
    {
        if ($this->isCsrfTokenValid('delete'.$institucion->getId(), $request->request->get('_token'))) {
            $entityManager->remove($institucion);
            $entityManager->flush();
        }

        return $this->redirectToRoute('app_institucion_index', [], Response::HTTP_SEE_OTHER);
    }
}
